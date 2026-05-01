-- Принимает часть имени или телефона и возвращает таблицу совпадений
CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    WHERE phonebook.name ILIKE '%' || p_pattern || '%' 
       OR phonebook.phone LIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;
-- Позволяет просматривать данные частями (страницами)
-- p_limit - сколько строк выдать, p_offset - сколько пропустить
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    ORDER BY id 
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;