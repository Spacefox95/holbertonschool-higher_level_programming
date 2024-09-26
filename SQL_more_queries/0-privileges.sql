-- List all privileges of MySQL users
 SHOW GRANTS FOR 'user_0d_1'@'localhost';
 SHOW GRANTS FOR 'user_0d_2'@'localhost';
 GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
