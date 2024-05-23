-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: db
-- Время создания: Май 23 2024 г., 06:10
-- Версия сервера: 8.0.37
-- Версия PHP: 8.2.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `medstat`
--

-- --------------------------------------------------------

--
-- Структура таблицы `analysis_analysis`
--

CREATE TABLE `analysis_analysis` (
  `id` bigint NOT NULL,
  `weight` double DEFAULT NULL,
  `girth` double DEFAULT NULL,
  `pulse` int DEFAULT NULL,
  `calories_pd` int DEFAULT NULL,
  `steps_pd` int DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `analysis_analysis`
--

INSERT INTO `analysis_analysis` (`id`, `weight`, `girth`, `pulse`, `calories_pd`, `steps_pd`, `date_created`, `user_id`) VALUES
(1, 85, 50, 125, 1250, 10000, '2024-05-01 07:04:53.000000', 1),
(2, 84, 46, 120, 2500, 12000, '2024-05-02 07:04:53.000000', 1),
(3, 83, 52, 194, 1550, 11000, '2024-05-01 07:04:53.000000', 1),
(4, 82, 47, 110, 3500, 15000, '2024-05-02 07:04:53.000000', 1),
(5, 88, 18, 128, 1288, 10800, '2024-05-05 07:51:34.000000', 1),
(6, 88, 18, 128, 1288, 10800, '2024-05-23 04:56:24.325536', 1),
(7, 88, 18, 128, 1288, 10800, '2024-05-23 04:58:14.252574', 1),
(8, 88, 18, 128, 1288, 10800, '2024-05-23 04:59:32.125034', 1),
(9, 88, 18, 128, 1288, 10800, '2024-05-23 04:59:42.577925', 1),
(10, 88, 18, 128, 1288, 10800, '2024-05-23 05:00:49.713632', 1),
(11, 88, 18, 128, 1288, 10800, '2024-05-23 05:01:02.739760', 1),
(12, 88, 18, 128, 1288, 10800, '2024-05-23 05:01:51.708767', 1),
(13, 88, 18, 128, 1288, 10800, '2024-05-23 05:02:07.099965', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add category', 7, 'add_category'),
(26, 'Can change category', 7, 'change_category'),
(27, 'Can delete category', 7, 'delete_category'),
(28, 'Can view category', 7, 'view_category'),
(29, 'Can add post', 8, 'add_post'),
(30, 'Can change post', 8, 'change_post'),
(31, 'Can delete post', 8, 'delete_post'),
(32, 'Can view post', 8, 'view_post'),
(33, 'Can add profile', 9, 'add_profile'),
(34, 'Can change profile', 9, 'change_profile'),
(35, 'Can delete profile', 9, 'delete_profile'),
(36, 'Can view profile', 9, 'view_profile'),
(37, 'Can add analysis', 10, 'add_analysis'),
(38, 'Can change analysis', 10, 'change_analysis'),
(39, 'Can delete analysis', 10, 'delete_analysis'),
(40, 'Can view analysis', 10, 'view_analysis');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$ohDbxEzsXFZ8tEHVvNCTLj$yZgHssaBJiLEssHjwC3b9rF5JO0N+TBPm9F+u+iQhMI=', '2024-05-23 04:24:22.423310', 0, 'websofter', '', '', 'mail.websofter@gmail.com', 0, 1, '2024-05-21 17:08:46.243690');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `blog_category`
--

CREATE TABLE `blog_category` (
  `id` bigint NOT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `blog_category`
--

INSERT INTO `blog_category` (`id`, `name`) VALUES
(1, 'Диета'),
(2, 'Тренировки');

-- --------------------------------------------------------

--
-- Структура таблицы `blog_post`
--

CREATE TABLE `blog_post` (
  `id` bigint NOT NULL,
  `slug` varchar(200) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `text` longtext,
  `status` varchar(10) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `date_updated` datetime(6) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `category_id` bigint NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `blog_post`
--

INSERT INTO `blog_post` (`id`, `slug`, `title`, `text`, `status`, `date_created`, `date_updated`, `image`, `category_id`, `user_id`) VALUES
(1, 'somw-post', 'Тренировки', 'Текст тренировок', '', '2024-05-22 03:01:30.000000', '2024-05-22 03:01:30.000000', NULL, 1, 1),
(2, 'dieta', 'Пост про диету', 'Текст поста про диету', '', '2024-05-22 03:01:30.000000', '2024-05-22 03:01:30.000000', NULL, 1, 1),
(3, 'моя-первая-статья', 'Моя первая статья', '4gf4tgtgt', 'PUBLISHED', '2024-05-22 16:50:08.230538', '2024-05-22 16:50:08.230538', 'uploads/1528370234_5_FVCovBS.jpg', 1, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

-- --------------------------------------------------------

--
-- Структура таблицы `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(10, 'analysis', 'analysis'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'blog', 'category'),
(8, 'blog', 'post'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(9, 'user', 'profile');

-- --------------------------------------------------------

--
-- Структура таблицы `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-05-21 17:06:48.740373'),
(2, 'auth', '0001_initial', '2024-05-21 17:06:49.264093'),
(3, 'admin', '0001_initial', '2024-05-21 17:06:49.405380'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-05-21 17:06:49.413780'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-21 17:06:49.436345'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-05-21 17:06:49.508985'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-05-21 17:06:49.571100'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-05-21 17:06:49.591561'),
(9, 'auth', '0004_alter_user_username_opts', '2024-05-21 17:06:49.601739'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-05-21 17:06:49.657035'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-05-21 17:06:49.662917'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-05-21 17:06:49.671029'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-05-21 17:06:49.766420'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-05-21 17:06:49.834679'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-05-21 17:06:49.849911'),
(16, 'auth', '0011_update_proxy_permissions', '2024-05-21 17:06:49.860860'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-05-21 17:06:49.922058'),
(18, 'blog', '0001_initial', '2024-05-21 17:06:50.117538'),
(19, 'sessions', '0001_initial', '2024-05-21 17:06:50.160790'),
(20, 'user', '0001_initial', '2024-05-21 17:06:50.247632'),
(21, 'blog', '0002_alter_post_image', '2024-05-23 04:03:16.407365'),
(22, 'analysis', '0001_initial', '2024-05-23 04:03:55.498340'),
(23, 'analysis', '0002_alter_analysis_date_created', '2024-05-23 04:51:50.607190');

-- --------------------------------------------------------

--
-- Структура таблицы `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ep8jymk4t9tutiwuxef4msppol6ef1px', '.eJxVjMsOwiAQRf-FtSG8BMal-34DGRiQqqFJaVfGf1eSLnR7z7nnxQLuWw17z2uYiV2YZKffLWJ65DYA3bHdFp6Wtq1z5EPhB-18Wig_r4f7F6jY68h60gKMQtJEpECYKNErl9wZUGcDUIS10hVnRbI6Ow-YtYpGfG8lCvb-AMmINxY:1sA006:Og2oB5ICRtMxGzoQzYUe2ZHgaC9ZfG8p8fUwgnQwsv0', '2024-06-06 04:24:22.428590');

-- --------------------------------------------------------

--
-- Структура таблицы `user_profile`
--

CREATE TABLE `user_profile` (
  `id` bigint NOT NULL,
  `age` int DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `user_profile`
--

INSERT INTO `user_profile` (`id`, `age`, `gender`, `birth_date`, `status`, `user_id`) VALUES
(1, NULL, NULL, NULL, 1, 1);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `analysis_analysis`
--
ALTER TABLE `analysis_analysis`
  ADD PRIMARY KEY (`id`),
  ADD KEY `analysis_analysis_user_id_c2741343_fk_auth_user_id` (`user_id`);

--
-- Индексы таблицы `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Индексы таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Индексы таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Индексы таблицы `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Индексы таблицы `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Индексы таблицы `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Индексы таблицы `blog_category`
--
ALTER TABLE `blog_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `blog_category_name_92eb1483_uniq` (`name`);

--
-- Индексы таблицы `blog_post`
--
ALTER TABLE `blog_post`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD UNIQUE KEY `blog_post_title_adf2f203_uniq` (`title`),
  ADD KEY `blog_post_category_id_c326dbf8_fk_blog_category_id` (`category_id`),
  ADD KEY `blog_post_user_id_710cc4d2_fk_auth_user_id` (`user_id`);

--
-- Индексы таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Индексы таблицы `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Индексы таблицы `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Индексы таблицы `user_profile`
--
ALTER TABLE `user_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `analysis_analysis`
--
ALTER TABLE `analysis_analysis`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT для таблицы `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT для таблицы `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `blog_category`
--
ALTER TABLE `blog_category`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `blog_post`
--
ALTER TABLE `blog_post`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT для таблицы `user_profile`
--
ALTER TABLE `user_profile`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `analysis_analysis`
--
ALTER TABLE `analysis_analysis`
  ADD CONSTRAINT `analysis_analysis_user_id_c2741343_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `blog_post`
--
ALTER TABLE `blog_post`
  ADD CONSTRAINT `blog_post_category_id_c326dbf8_fk_blog_category_id` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`id`),
  ADD CONSTRAINT `blog_post_user_id_710cc4d2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `user_profile`
--
ALTER TABLE `user_profile`
  ADD CONSTRAINT `user_profile_user_id_8fdce8e2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
