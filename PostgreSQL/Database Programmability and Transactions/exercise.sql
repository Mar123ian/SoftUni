--EXERCISE 12
CREATE TABLE logs(
    id SERIAL PRIMARY KEY,
    account_id INTEGER,
    old_sum NUMERIC(19,4),
    new_sum NUMERIC(19,4)
);

CREATE OR REPLACE FUNCTION trigger_fn_insert_new_entry_into_logs()
RETURNS TRIGGER AS
$$
    BEGIN
       INSERT INTO logs(account_id, old_sum, new_sum)
       VALUES (OLD.id, OLD.balance, NEW.balance);

       RETURN NEW;
    END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_account_balance_change
AFTER UPDATE ON accounts FOR EACH ROW WHEN ( NEW.balance != OLD.balance ) EXECUTE FUNCTION trigger_fn_insert_new_entry_into_logs();

--EXERCISE 13
CREATE TABLE notification_emails(
    id SERIAL PRIMARY KEY,
    recipient_id INTEGER,
    subject TEXT,
    body TEXT
);

CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER AS
$$
    BEGIN
        IF NEW.new_sum!=OLD.new_sum THEN
            INSERT INTO notification_emails(recipient_id, subject, body)
            VALUES (NEW.account_id,
                    concat('Balance change for account: ', NEW.account_id),
                    concat('On ', CURRENT_DATE, ' your balance was changed from ', OLD.new_sum, ' to ', NEW.new_sum, '.'));
        ELSIF NEW.old_sum!=OLD.old_sum THEN
             INSERT INTO notification_emails(recipient_id, subject, body)
            VALUES (NEW.account_id, concat('Balance change for account: ', NEW.account_id), concat('On ', CURRENT_DATE, ' your balance was changed from ', OLD.old_sum, ' to ', NEW.old_sum, '.'));
        END IF;

        RETURN NEW;

    END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER tr_send_email_on_balance_change
AFTER UPDATE ON logs FOR EACH ROW WHEN ( NEW.new_sum != OLD.new_sum ) EXECUTE FUNCTION trigger_fn_send_email_on_balance_change();

--EXERCISE 8
CREATE OR REPLACE PROCEDURE sp_deposit_money(account_id INTEGER, money_amount NUMERIC(19,4))
AS
$$
    BEGIN
        UPDATE accounts
        SET balance=balance+money_amount
        WHERE id=account_id;
    END;
$$
LANGUAGE plpgsql;

--EXERCISE 9
CREATE OR REPLACE PROCEDURE sp_withdraw_money(account_id INTEGER, money_amount NUMERIC(19,4))
AS
$$
    DECLARE
        account_balance INTEGER;
    BEGIN
        account_balance:=(SELECT balance FROM accounts WHERE id=account_id);

        IF account_balance>=money_amount THEN
            UPDATE accounts
            SET balance=balance-money_amount
            WHERE id=account_id;

            RETURN;
        END IF ;

        RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;

    END;
$$
LANGUAGE plpgsql;

--EXERCISE 10
CREATE OR REPLACE PROCEDURE sp_transfer_money(sender_id INTEGER, receiver_id INTEGER, amount NUMERIC(19,4))
AS
$$
    DECLARE
        sender_old_balance NUMERIC;
        sender_new_balance NUMERIC;
        receiver_old_balance NUMERIC;
        receiver_new_balance NUMERIC;

    BEGIN
        sender_old_balance:=(SELECT balance FROM accounts WHERE id=sender_id);
        CALL sp_withdraw_money(sender_id, amount);
        sender_new_balance:=(SELECT balance FROM accounts WHERE id=sender_id);

        IF sender_new_balance!=sender_old_balance-amount THEN
            ROLLBACK;
            RETURN;
        END IF;

        receiver_old_balance:=(SELECT balance FROM accounts WHERE id=receiver_id);
        CALL sp_deposit_money(receiver_id, amount);
        receiver_new_balance:=(SELECT balance FROM accounts WHERE id=receiver_id);

        IF receiver_new_balance!=receiver_old_balance+amount THEN
            ROLLBACK;
            RETURN;
        END IF;

        COMMIT;

    END;
$$
LANGUAGE plpgsql;



