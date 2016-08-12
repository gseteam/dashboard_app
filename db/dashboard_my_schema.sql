DROP TABLE IF EXISTS newsletter_student_model;
CREATE TABLE IF NOT EXISTS `newsletter_student_model` (
    `Id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` varchar(200) NOT NULL
);
DROP TABLE IF EXISTS django_session;
CREATE TABLE IF NOT EXISTS `django_session` (
    `session_key` varchar(40) NOT NULL PRIMARY KEY,
    `session_data` text NOT NULL,
    `expire_date` datetime NOT NULL
);
DROP TABLE IF EXISTS django_migrations;
CREATE TABLE IF NOT EXISTS `django_migrations` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `app` varchar(255) NOT NULL, `name` varchar(255) NOT NULL, `applied` datetime NOT NULL);
DROP TABLE IF EXISTS django_content_type;
CREATE TABLE IF NOT EXISTS `django_content_type` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `app_label` varchar(100) NOT NULL, `model` varchar(100) NOT NULL);
DROP TABLE IF EXISTS django_admin_log;
CREATE TABLE IF NOT EXISTS `django_admin_log` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `object_id` text NULL, `object_repr` varchar(200) NOT NULL, `action_flag` smallint unsigned NOT NULL, `change_message` text NOT NULL, `content_type_id` integer NULL REFERENCES `django_content_type` (`id`), `user_id` integer NOT NULL REFERENCES `auth_user` (`id`), `action_time` datetime NOT NULL);
DROP TABLE IF EXISTS auth_user_user_permissions;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `user_id` integer NOT NULL,
    `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`),
    UNIQUE (`user_id`, `permission_id`)
);
DROP TABLE IF EXISTS auth_user_groups;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `user_id` integer NOT NULL,
    `group_id` integer NOT NULL REFERENCES `auth_group` (`id`),
    UNIQUE (`user_id`, `group_id`)
);
DROP TABLE IF EXISTS auth_user;
CREATE TABLE IF NOT EXISTS `auth_user` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `password` varchar(128) NOT NULL, `last_login` datetime NULL, `is_superuser` bool NOT NULL, `first_name` varchar(30) NOT NULL, `last_name` varchar(30) NOT NULL, `email` varchar(254) NOT NULL, `is_staff` bool NOT NULL, `is_active` bool NOT NULL, `date_joined` datetime NOT NULL, `username` varchar(30) NOT NULL UNIQUE);
DROP TABLE IF EXISTS auth_permission;
CREATE TABLE IF NOT EXISTS `auth_permission` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `content_type_id` integer NOT NULL REFERENCES `django_content_type` (`id`), `codename` varchar(100) NOT NULL, `name` varchar(255) NOT NULL);
DROP TABLE IF EXISTS auth_group_permissions;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `group_id` integer NOT NULL,
    `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`),
    UNIQUE (`group_id`, `permission_id`)
);
DROP TABLE IF EXISTS auth_group;
CREATE TABLE IF NOT EXISTS `auth_group` (
    `id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` varchar(80) NOT NULL UNIQUE
);
DROP TABLE IF EXISTS app;
CREATE TABLE IF NOT EXISTS `app1_settings_model` (`Project_Allocated` varchar(100) NOT NULL, `Id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT);
DROP TABLE IF EXISTS app;
CREATE TABLE IF NOT EXISTS `app1_people_model` (`Id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `name` varchar(100) NOT NULL, `vacation_plan` varchar(100) NOT NULL, `visa_status` varchar(100) NOT NULL);
DROP TABLE IF EXISTS app;
CREATE TABLE IF NOT EXISTS `app1_detail_model` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `Act_name` varchar(100) NOT NULL, `emp_name` varchar(100) NOT NULL);
DROP TABLE IF EXISTS app;
CREATE TABLE IF NOT EXISTS `app1_activity_model` (`Activity_Id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `Activity_Name` varchar(100) NOT NULL, `Activity_type` varchar(100) NOT NULL, `state` varchar(100) NOT NULL, `Customer_name` varchar(100) NOT NULL, `Description` varchar(2500) NOT NULL);
CREATE INDEX `django_session_b7b81f0c` ON `django_session` (`expire_date`);
CREATE INDEX `django_admin_log_e8701ad4` ON `django_admin_log` (`user_id`);
CREATE INDEX `django_admin_log_417f1b1c` ON `django_admin_log` (`content_type_id`);
CREATE INDEX `auth_user_user_permissions_83d7f98b` ON `auth_user_user_permissions` (`permission_id`);
CREATE INDEX `auth_user_user_permissions_6340c63c` ON `auth_user_user_permissions` (`user_id`);
CREATE INDEX `auth_user_groups_6340c63c` ON `auth_user_groups` (`user_id`);
CREATE INDEX `auth_user_groups_5f412f9a` ON `auth_user_groups` (`group_id`);
CREATE INDEX `auth_permission_417f1b1c` ON `auth_permission` (`content_type_id`);
CREATE INDEX `auth_group_permissions_83d7f98b` ON `auth_group_permissions` (`permission_id`);
CREATE INDEX `auth_group_permissions_5f412f9a` ON `auth_group_permissions` (`group_id`);
