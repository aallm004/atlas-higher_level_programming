-- creates server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFITED BY 'user_0d_1_pwd';
GRANT ALL PRIVELAGES ON *.* TO 'user_0d_1'@'localhost';