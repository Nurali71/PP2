-- Если контакт с таким именем уже есть — обновляем телефон.
-- Если нет — создаем новую запись.
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;
-- Принимает два массива: список имен и список телефонов.
-- Проверяет, чтобы номер был не короче 11 символов.
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(p_names VARCHAR[], p_phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_length(p_names, 1) LOOP
        -- Простая проверка валидности номера (длина)
        IF length(p_phones[i]) >= 11 THEN
            INSERT INTO phonebook(name, phone) 
            VALUES(p_names[i], p_phones[i])
            ON CONFLICT (phone) DO NOTHING;
        ELSE
            -- Выводит предупреждение в консоль базы, если номер плохой
            RAISE NOTICE 'Invalid phone number for user %: %', p_names[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$;
-- Процедура удаления по имени ИЛИ телефону
CREATE OR REPLACE PROCEDURE delete_contact_v2(p_search VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE name = p_search OR phone = p_search;
END;
$$;