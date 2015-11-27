-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 27-11-2015 a las 18:14:03
-- Versión del servidor: 5.5.43-0ubuntu0.14.04.1
-- Versión de PHP: 5.5.9-1ubuntu4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `perucall`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agentebase`
--

CREATE TABLE IF NOT EXISTS `agentebase` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `agente` int(100) DEFAULT NULL,
  `base` int(100) DEFAULT NULL,
  `tiniciogestion` datetime DEFAULT NULL,
  `tfingestion` datetime DEFAULT NULL,
  `duracion` int(11) DEFAULT NULL,
  `comentario` mediumtext,
  `facuerdo` datetime DEFAULT NULL,
  `macuerdo` int(100) DEFAULT NULL,
  `status` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `agente` (`agente`),
  KEY `base` (`base`),
  KEY `status` (`status`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Volcado de datos para la tabla `agentebase`
--

INSERT INTO `agentebase` (`id`, `agente`, `base`, `tiniciogestion`, `tfingestion`, `duracion`, `comentario`, `facuerdo`, `macuerdo`, `status`) VALUES
(1, 14, 6, '2015-11-27 21:33:32', NULL, NULL, 'trtrt', '2016-02-01 00:00:00', 54534, 6),
(2, 14, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 21, 7, '2015-11-27 22:33:56', NULL, NULL, NULL, NULL, NULL, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agentes`
--

CREATE TABLE IF NOT EXISTS `agentes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `anexo` int(11) DEFAULT NULL,
  `fono` int(11) DEFAULT NULL,
  `tiempo` time DEFAULT '00:00:00',
  `atendidas` int(11) DEFAULT '0',
  `contactadas` int(11) DEFAULT '0',
  `estado` int(11) DEFAULT '1',
  `user` int(100) DEFAULT NULL,
  `supervisor` int(100) DEFAULT NULL,
  `disponible` int(100) DEFAULT '0',
  `calificacion` int(100) DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `user` (`user`),
  KEY `supervisor` (`supervisor`),
  KEY `estado` (`estado`),
  KEY `calificacion` (`calificacion`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=22 ;

--
-- Volcado de datos para la tabla `agentes`
--

INSERT INTO `agentes` (`id`, `anexo`, `fono`, `tiempo`, `atendidas`, `contactadas`, `estado`, `user`, `supervisor`, `disponible`, `calificacion`) VALUES
(14, NULL, NULL, '00:00:00', 700, 350, 1, 89, NULL, NULL, NULL),
(15, NULL, NULL, '00:00:00', 0, 0, 1, 90, NULL, NULL, NULL),
(16, NULL, NULL, '00:00:00', 0, 0, 1, 96, NULL, NULL, NULL),
(17, NULL, NULL, '00:00:00', 0, 0, 1, 97, NULL, NULL, NULL),
(18, NULL, NULL, '00:00:00', 0, 0, 1, 98, NULL, NULL, NULL),
(19, NULL, NULL, '00:00:00', 0, 0, 1, 99, NULL, NULL, NULL),
(20, NULL, NULL, '00:00:00', 0, 0, 1, 100, NULL, NULL, NULL),
(21, NULL, NULL, '00:00:00', 0, 0, 1, 101, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agentescampanias`
--

CREATE TABLE IF NOT EXISTS `agentescampanias` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `agente` int(100) NOT NULL,
  `campania` int(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `agente` (`agente`),
  KEY `campania` (`campania`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=202 ;

--
-- Volcado de datos para la tabla `agentescampanias`
--

INSERT INTO `agentescampanias` (`id`, `agente`, `campania`) VALUES
(180, 14, 54),
(181, 15, 54),
(183, 15, 8),
(187, 14, 57),
(188, 15, 57),
(189, 14, 63),
(190, 15, 63),
(199, 19, 66),
(200, 20, 66),
(201, 21, 66);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=19 ;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_spanish_ci NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) DEFAULT NULL,
  `username` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_spanish_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `email` varchar(75) COLLATE utf8_spanish_ci DEFAULT NULL,
  `is_staff` tinyint(1) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `date_joined` datetime DEFAULT NULL,
  `empresa` int(100) DEFAULT '1',
  `nivel` int(11) NOT NULL DEFAULT '4',
  `telefono` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `nivel` (`nivel`),
  KEY `empresa` (`empresa`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=102 ;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `empresa`, `nivel`, `telefono`) VALUES
(2, 'pbkdf2_sha256$15000$emGDFLEMc6GK$mfEdE/RXj7/Ixs7DSIY86vR4oHBYsjsTQ9tdLogTBI8=', '2015-10-12 16:42:02', 0, 'joel', 'Joelinho', '', '', 0, 1, '2015-10-12 16:41:07', 2, 2, NULL),
(3, 'pbkdf2_sha256$12000$1ee3TNce9VKq$rmiUYRobIm+hIigZABIXDWGWkC6FUQiCECE8DHSh4a8=', '2015-10-27 22:30:55', 0, 'viewCall', 'Berta', '', '', 0, 1, '2015-10-27 22:30:55', 3, 1, NULL),
(8, 'pbkdf2_sha256$15000$R6A1kAjrrj24$DKEGqrFG4doN/tvYg2A5p2NnunS3UBKymViGMXjP91A=', '2015-11-26 17:13:36', 0, 'manager', 'Elizabet', '', '', 0, 1, '2015-10-30 17:28:49', 2, 4, NULL),
(37, 'pbkdf2_sha256$15000$l8MUv7ReZfZI$Dg3DXLA30+y3IYKUIKNWRxnvvBSgoNuBfifeAlyIXAo=', '2015-11-04 23:22:35', 0, 'Carlota', '', '', 'carlota@perucall.com', 0, 1, '2015-11-04 23:22:35', 53, 1, NULL),
(38, 'pbkdf2_sha256$15000$fkRolrDbTOY2$W9DqqYy+u4pRznedSkxNhkYay7sjLNZqwHBZbN25VAQ=', '2015-11-04 23:24:46', 0, 'asde', '', '', 'brujas@gmail.com', 0, 1, '2015-11-04 23:24:46', 53, 1, NULL),
(39, 'pbkdf2_sha256$15000$sK8ebMBxLGHq$vJfUpu8Mim13WLIVwkR3xBAZ5mFBXnSLsbbZq6s74xo=', '2015-11-05 02:14:27', 0, 'lucho', 'lucho', '', 'joelunmsm2@gmail.com', 0, 1, '2015-11-05 02:14:27', 54, 1, NULL),
(86, 'pbkdf2_sha256$15000$JAtGrjW1aWVC$B8Lcxz7SyPjNuWOjfmQDRRLXE9dqZl4ryMW3BiAagb4=', '2015-11-27 15:04:59', 0, 'admin', 'Hugo', '', '', 0, 1, '2015-11-22 01:31:48', 53, 1, 12121),
(87, 'pbkdf2_sha256$15000$G6eGxwyuxwOc$OW76zec9G73yDpkLDYeAqEj4fyfy/66L8UOwotEfNf8=', '2015-11-27 22:26:24', 0, 'supervisor', 'Federica', '', '', 0, 1, '2015-11-22 01:45:57', 53, 2, 123),
(89, 'pbkdf2_sha256$15000$S55ukFOMqFjT$QAq9ACzZEVgTxI6D47LzlhR2r6L6qrXYoJlyqQTef6Q=', '2015-11-26 14:55:26', 0, 'agente', 'Cesar', '', '', 0, 1, '2015-11-22 01:56:00', 53, 3, 32131),
(90, 'pbkdf2_sha256$15000$ur85YVflSuWh$0dfeb0I/My0hwsK9bgLAkyRySMqpxG/ypy8Rhc4xETk=', '2015-11-22 01:59:43', 0, 'ania', 'Ania', '', '', 0, 1, '2015-11-22 01:59:43', 53, 3, 33131),
(91, 'pbkdf2_sha256$15000$15Ziw4FUFv3M$DVoJUa2Fdbw01TjGgBgGF5815QM5qJZr/f4JwqObHr8=', '2015-11-24 17:37:01', 0, 'joel123@gmail.com', 'joel', '', '', 0, 1, '2015-11-24 17:37:01', 53, 2, 123),
(92, 'pbkdf2_sha256$15000$ynX8KopAjvgd$ku8w9XgLYRRdl7R5ub7cc0VLl4GGN5ZloCfWksfBlww=', '2015-11-24 17:40:00', 0, 'dff', 'ew', '', '', 0, 1, '2015-11-24 17:40:00', 53, 2, 122),
(93, 'pbkdf2_sha256$15000$jxfhJEU7WaeO$tvLL/mPqDUAWhEiY5wRUPcQGrqLpoNPqUjOjNSIYi64=', '2015-11-24 17:40:50', 0, '5656', '656', '', '', 0, 1, '2015-11-24 17:40:50', 53, 2, 123),
(94, 'pbkdf2_sha256$15000$ADSec2EQjLRf$wCw9zdstT0TPhFApX29xPIaqX5bh8qbeTwI99wEYIlM=', '2015-11-24 17:45:10', 0, 'rtr', 'fdfd', '', '', 0, 1, '2015-11-24 17:45:10', 53, 2, 1212),
(95, 'pbkdf2_sha256$15000$gBdNy5SlViIr$7+0T5vBuTETot8Nvm6T45P9iL/F84jNuJtdNATpCmfE=', '2015-11-24 17:48:23', 0, 'kolo', 'Kolito', '', '', 0, 1, '2015-11-24 17:48:23', 53, 2, 13),
(96, 'pbkdf2_sha256$15000$nfoidoYGu5k2$9W2sOgQsKlJtwDi6HWvXHqlcMyrq3TCbKq/Uk/Ewj5s=', '2015-11-26 21:06:33', 0, 'joel1@gmail.com', 'Joel', '', '', 0, 1, '2015-11-26 21:06:33', 53, 3, 123),
(97, 'pbkdf2_sha256$15000$SQpsthaJxwQk$8EuI1+Z40EW/AiHRl6kSPf26zjWVxnod5EVry2tM02I=', '2015-11-26 21:06:56', 0, 'joel2@gmail.com', 'Joel2', '', '', 0, 1, '2015-11-26 21:06:56', 53, 3, 123),
(98, 'pbkdf2_sha256$15000$gaTbS4VvL2I3$YHJdPuthIYPLTduGw5O8hVsbO8KdDMtsuhfjBMwf6kg=', '2015-11-26 21:07:16', 0, 'joel3@gmail.com', 'Joel3', '', '', 0, 1, '2015-11-26 21:07:16', 53, 3, 1234),
(99, 'pbkdf2_sha256$15000$7N8ByyjbDqid$HTbJAcjbXy9hTVTzgs/e0YI9qANPMXlE//9xAgHT4gU=', '2015-11-26 21:07:48', 0, 'joel4@gmail.com', 'Joel4', '', '', 0, 1, '2015-11-26 21:07:48', 53, 3, 123),
(100, 'pbkdf2_sha256$15000$DOiB6Ffmtzmz$8uZTUlCYJkNhB0nGy/lzyvl+ot7eiwMTUoEzxyvCLM4=', '2015-11-26 21:08:07', 0, 'joel5@gmail.com', 'joel5', '', '', 0, 1, '2015-11-26 21:08:07', 53, 3, 123),
(101, 'pbkdf2_sha256$15000$P6osweciH0au$u11eJXB8zXI7Gc6PSlkfFx4F/gDiwbvujXpnZamjnus=', '2015-11-26 21:20:19', 0, 'joel9@gmail.com', '123', '', '', 0, 1, '2015-11-26 21:20:19', 53, 3, 323);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `base`
--

CREATE TABLE IF NOT EXISTS `base` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `telefono` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `orden` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cliente` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `id_cliente` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `status_a` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `status_b` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `status_c` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `status_d` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `status_e` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `status_f` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `status_g` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `status_h` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `status` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `campania` int(100) DEFAULT NULL,
  `resultado` int(100) DEFAULT NULL,
  `agente` int(100) DEFAULT NULL,
  `duracion` int(100) DEFAULT NULL,
  `detalle` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `monto` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `tiniciogestion` datetime DEFAULT NULL,
  `tfingestion` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `campania` (`campania`),
  KEY `resultado` (`resultado`),
  KEY `agente` (`agente`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=167 ;

--
-- Volcado de datos para la tabla `base`
--

INSERT INTO `base` (`id`, `telefono`, `orden`, `cliente`, `id_cliente`, `status_a`, `status_b`, `status_c`, `status_d`, `status_e`, `status_f`, `status_g`, `status_h`, `status`, `campania`, `resultado`, `agente`, `duracion`, `detalle`, `monto`, `fecha`, `tiniciogestion`, `tfingestion`) VALUES
(1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'AYACUCHO', 'DIRECTO', 'SCORE C', '1', 8, 4, NULL, 8, '', NULL, NULL, NULL, NULL),
(2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'LIMA', 'NUEVO', 'SCORE C', '0', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'LIMA', 'INDIRECTO', 'SCORE C', '0', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'AYACUCHO', 'DIRECTO', 'SCORE C', '1', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(5, '996867686.0', '1.0', 'u''PITILLO BENAVIDES''', '41909034.0', 'u''VISA CLASICA''', 'u''4457896457851660''', '9671.35', '8634.75', '36.0', 'u''AREQUIPA''', 'u''DIRECTO''', 'u''SCORE A''', '0', 8, 3, 14, 9, '', NULL, NULL, NULL, NULL),
(6, '979864789.0', '2.0', 'u''PITILLO BENAVIDES''', '41909034.0', 'u''MASTERCARD ORO''', 'u''5598676334682245''', '6789.45', '5987.36', '15.0', 'u''AREQUIPA''', 'u''DIRECTO''', 'u''SCORE A''', '1', 8, 11, 14, 888, '', NULL, NULL, '2015-11-27 17:50:50', NULL),
(7, '975874897.0', '1.0', 'u''TOTO TERRY''', '67985478.0', 'u''AMERICAN EXPRESS''', 'u''6689745898756981''', '1687.35', '1168.95', '67.0', 'u''AYACUCHO''', 'u''INDIRECTO''', 'u''SCORE C''', '1', 8, 7, 21, NULL, '', NULL, NULL, NULL, NULL),
(8, '943215048.0', '1.0', 'u''ALBERTO BEINGOLEA''', '88749235.0', 'u''PRESTAMO PERSONAL''', 'u''00026987469''', '10369.48', '9168.74', '69.0', 'u''LIMA''', 'u''NUEVO''', 'u''SCORE B''', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(9, '967810348.0', '1.0', 'u''POLO CAMPO''', '77495678.0', 'u''CREDITO VEHICULAR''', 'u''99647952658''', '32697.48', '28367.14', '49.0', 'u''AYACUCHO''', 'u''DIRECTO''', 'u''SCORE C''', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(10, '991357001.0', '2.0', 'u''POLO CAMPO''', '77495678.0', 'u''CREDITO HIOPTECARIO''', 'u''99886974695''', '105369.45', '94698.36', '102.0', 'u''AYACUCHO''', 'u''INDIRECTO''', 'u''SCORE C''', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(11, '996867689.0', '1.0', 'u''PITILLO BENAVIDES''', '41909034.0', 'u''VISA CLASICA''', 'u''4457896457851660''', '9671.35', '8634.75', '36.0', 'u''AREQUIPA''', 'u''DIRECTO''', 'u''SCORE A''', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(12, '979864782.0', '2.0', 'u''PITILLO BENAVIDES''', '41909034.0', 'u''MASTERCARD ORO''', 'u''5598676334682245''', '6789.45', '5987.36', '15.0', 'u''AREQUIPA''', 'u''DIRECTO''', 'u''SCORE A''', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(13, '975874896.0', '1.0', 'u''Cesar''', '67985478.0', 'u''AMERICAN EXPRESS''', 'u''6689745898756981''', '1687.35', '1168.95', '67.0', 'u''AYACUCHO''', 'u''INDIRECTO''', 'u''SCORE C''', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(14, '9432150483.0', '1.0', 'u''Juan''', '88749235.0', 'u''PRESTAMO PERSONAL''', 'u''00026987469''', '10369.48', '9168.74', '69.0', 'u''LIMA''', 'u''NUEVO''', 'u''SCORE B''', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(15, '967810348.0', '1.0', 'u''Carlos''', '77495678.0', 'u''CREDITO VEHICULAR''', 'u''99647952658''', '32697.48', '28367.14', '49.0', 'u''AYACUCHO''', 'u''DIRECTO''', 'u''SCORE C''', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(16, '991357001.0', '2.0', 'u''Ana''', '77495678.0', 'u''CREDITO HIOPTECARIO''', 'u''99886974695''', '105369.45', '94698.36', '102.0', 'u''AYACUCHO''', 'u''INDIRECTO''', 'u''SCORE C''', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(17, '996867686.0', '1.0', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36.0', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(18, '979864789.0', '2.0', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15.0', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(19, '975874897.0', '1.0', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67.0', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(20, '943215048.0', '1.0', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69.0', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(21, '967810348.0', '1.0', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49.0', 'AYACUCHO', 'DIRECTO', 'SCORE C', '1', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(22, '991357001.0', '2.0', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102.0', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(23, '996867689.0', '1.0', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36.0', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(24, '979864782.0', '2.0', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15.0', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(25, '975874896.0', '1.0', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67.0', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(26, '9432150483.0', '1.0', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69.0', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(27, '967810348.0', '1.0', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49.0', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(28, '991357001.0', '2.0', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102.0', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(29, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(30, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(31, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(32, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(33, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(34, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(35, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(36, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(37, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(38, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(39, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(40, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(41, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(42, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(43, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(44, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(45, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(46, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(47, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(48, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(49, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(50, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(51, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(52, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(53, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(54, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(55, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(56, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(57, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(58, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(59, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(60, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(61, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(62, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(63, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(64, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(65, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(66, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(67, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(68, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(69, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(70, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(71, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(72, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(73, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(74, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(75, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(76, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(77, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(78, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(79, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(80, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(81, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 8, 4, NULL, NULL, '', NULL, NULL, NULL, NULL),
(82, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'DIRECTO', 'SCORE C', '1', 8, 1, NULL, NULL, '', NULL, NULL, NULL, NULL),
(83, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(84, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(85, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(86, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(87, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(88, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(89, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(90, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(91, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(92, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(93, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(94, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(95, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(96, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(97, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(98, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(99, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(100, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(101, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(102, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(103, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(104, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(105, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(106, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(107, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(108, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(109, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(110, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(111, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(112, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(113, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(114, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(115, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(116, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(117, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(118, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(119, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(120, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(121, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(122, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(123, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(124, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(125, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(126, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(127, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(128, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(129, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(130, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 60, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(131, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(132, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(133, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(134, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(135, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(136, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(137, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(138, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(139, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(140, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(141, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(142, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 61, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(143, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(144, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(145, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(146, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(147, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(148, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(149, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(150, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(151, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(152, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(153, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(154, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 63, 7, NULL, NULL, '', NULL, NULL, NULL, NULL),
(155, '996867686', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(156, '979864789', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(157, '975874897', '1', 'TOTO TERRY', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(158, '943215048', '1', 'ALBERTO BEINGOLEA', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(159, '967810348', '1', 'POLO CAMPO', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(160, '991357001', '2', 'POLO CAMPO', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(161, '996867689', '1', 'PITILLO BENAVIDES', '41909034.0', 'VISA CLASICA', '4457896457851660', '9671.35', '8634.75', '36', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(162, '979864782', '2', 'PITILLO BENAVIDES', '41909034.0', 'MASTERCARD ORO', '5598676334682245', '6789.45', '5987.36', '15', 'AREQUIPA', 'DIRECTO', 'SCORE A', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(163, '975874896', '1', 'Cesar', '67985478.0', 'AMERICAN EXPRESS', '6689745898756981', '1687.35', '1168.95', '67', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(164, '9432150483', '1', 'Juan', '88749235.0', 'PRESTAMO PERSONAL', '00026987469', '10369.48', '9168.74', '69', 'LIMA', 'NUEVO', 'SCORE B', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(165, '967810348', '1', 'Carlos', '77495678.0', 'CREDITO VEHICULAR', '99647952658', '32697.48', '28367.14', '49', 'AYACUCHO', 'DIRECTO', 'SCORE C', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL),
(166, '991357001', '2', 'Ana', '77495678.0', 'CREDITO HIOPTECARIO', '99886974695', '105369.45', '94698.36', '102', 'AYACUCHO', 'INDIRECTO', 'SCORE C', '', 66, 7, NULL, NULL, '', '', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificacion`
--

CREATE TABLE IF NOT EXISTS `calificacion` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `calificacion`
--

INSERT INTO `calificacion` (`id`, `tipo`, `descripcion`) VALUES
(1, 'DI', 'Consulta en tramite'),
(2, 'DI', 'Contacto sin promesa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `campania`
--

CREATE TABLE IF NOT EXISTS `campania` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha cargada` datetime DEFAULT NULL,
  `usuario` int(11) DEFAULT NULL,
  `estado` text COLLATE utf8_spanish_ci,
  `nombre` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `troncal` int(100) DEFAULT NULL,
  `canales` int(100) DEFAULT '2',
  `timbrados` int(100) DEFAULT NULL,
  `htinicio` time DEFAULT NULL,
  `htfin` time DEFAULT NULL,
  `mxllamada` int(100) DEFAULT '2',
  `llamadaxhora` int(100) DEFAULT '25',
  `hombreobjetivo` int(100) DEFAULT '80',
  `archivo` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `supervisor` int(100) DEFAULT '1',
  `cartera` int(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario` (`usuario`),
  KEY `supervisor` (`supervisor`),
  KEY `cartera` (`cartera`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=67 ;

--
-- Volcado de datos para la tabla `campania`
--

INSERT INTO `campania` (`id`, `fecha cargada`, `usuario`, `estado`, `nombre`, `troncal`, `canales`, `timbrados`, `htinicio`, `htfin`, `mxllamada`, `llamadaxhora`, `hombreobjetivo`, `archivo`, `supervisor`, `cartera`) VALUES
(8, '2015-11-04 22:37:59', 8, '', 'Pastillas LSD', 1, 12, 12, '01:00:00', '01:00:00', 12, 12, 212, 'files/settings_yi1cy1I.jsonp', NULL, NULL),
(9, '2015-11-04 22:42:44', 8, '', 'Viagra', 12, 212, 21, '01:00:00', '01:00:00', 2, 21, 213, 'files/C6AILKT_UqlkwvU.json', NULL, NULL),
(54, '2015-11-22 03:46:17', 87, '', 'Los indecentes', NULL, 1, 4, '01:00:00', '01:00:00', 2, 4, 80, 'files/Libro1_mWRao84.xlsx', 27, NULL),
(55, '2015-11-24 19:12:56', 87, '', 'Sapos', NULL, 12, 4, '08:00:00', '19:00:00', 2, 4, 80, 'joel_OsFnxNZ_1.xlsx', 27, 20),
(56, '2015-11-24 19:14:32', 87, '', 'Manitos', NULL, 22, 4, '08:00:00', '19:00:00', 2, 4, 80, 'files/joel_OsFnxNZ_1_11fF7Dh.xlsx', 27, 20),
(57, '2015-11-24 19:19:56', 87, '', 'Robots', NULL, 1, 4, '08:00:00', '19:00:00', 2, 4, 80, 'files/joel_OsFnxNZ_1_Shm6OuX.xlsx', 27, 20),
(58, '2015-11-24 19:53:13', 87, '', 'Borrachitos', NULL, 22, 4, '08:00:00', '19:00:00', 2, 4, 80, 'files/joel_OsFnxNZ_1_HJHYlEc.xlsx', 27, 20),
(59, '2015-11-24 19:53:53', 87, '', 'Pata', NULL, 1, 4, '08:00:00', '19:00:00', 2, 4, 80, 'files/joel_OsFnxNZ_1_oJXItpe.xlsx', 30, 20),
(60, '2015-11-24 19:56:06', 87, '', 'Ratoncitos', NULL, 12, 4, '08:00:00', '19:00:00', 2, 4, 80, 'files/joel_OsFnxNZ_1_UUCyiBH.xlsx', 27, 20),
(61, '2015-11-24 20:19:31', 87, '', 'Gatitos', NULL, 5, 4, '08:00:00', '19:00:00', 2, 4, 80, 'files/joel_OsFnxNZ_1_YslbsaK.xlsx', 27, 20),
(62, '2015-11-24 20:34:17', 87, '', 'Monitos', NULL, 3, 4, '08:00:00', '19:00:00', 2, 4, 80, 'files/joel_OsFnxNZ_1_2OEslxC.xlsx', 30, 20),
(63, '2015-11-24 20:34:46', 87, '', 'Chanchitos', NULL, 3, 4, '08:00:00', '19:00:00', 2, 4, 80, 'files/joel_OsFnxNZ_1_cNVElvq.xlsx', 27, 20),
(64, '2015-11-26 15:55:36', 87, '', 'Pinturas', NULL, 2, 4, '08:00:00', '19:00:00', 2, 4, 80, 'joel_OsFnxNZ_1.xlsx', 27, 20),
(65, '2015-11-26 17:17:04', 87, '', 'Teclado', NULL, 4, 4, '08:00:00', '19:00:00', 2, 4, 80, 'joel_OsFnxNZ_1.xlsx', 27, 20),
(66, '2015-11-26 17:19:51', 87, '', 'Peru', NULL, 2, 4, '08:00:00', '19:00:00', 2, 4, 80, 'files/joel_OsFnxNZ_1_4NqoHCk.xlsx', 27, 20);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cartera`
--

CREATE TABLE IF NOT EXISTS `cartera` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=23 ;

--
-- Volcado de datos para la tabla `cartera`
--

INSERT INTO `cartera` (`id`, `nombre`) VALUES
(1, 'Unique'),
(2, 'Saga'),
(3, 'Chifa Chaolin'),
(4, 'Restorant Don Gato'),
(5, 'Pilsen'),
(6, 'Nestle'),
(7, 'PeruVeloz'),
(8, 'Cartera'),
(9, 'ZzZ'),
(11, 'CcccCC'),
(12, 'Holaaa'),
(13, 'Sui'),
(14, 'Shaga'),
(15, 'Meitru'),
(16, 'Nestle'),
(17, 'Gloria'),
(18, 'Ford'),
(19, 'Nestle'),
(20, 'Backus'),
(21, 'Frecuencia Latina'),
(22, 'Totus');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carteraempresa`
--

CREATE TABLE IF NOT EXISTS `carteraempresa` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `cartera` int(100) NOT NULL,
  `empresa` int(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cartera` (`cartera`),
  KEY `empresa` (`empresa`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=21 ;

--
-- Volcado de datos para la tabla `carteraempresa`
--

INSERT INTO `carteraempresa` (`id`, `cartera`, `empresa`) VALUES
(12, 14, 2),
(13, 15, 2),
(14, 16, 54),
(15, 17, 54),
(16, 18, 54),
(17, 19, 53),
(18, 20, 53),
(19, 21, 53),
(20, 22, 53);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `data`
--

CREATE TABLE IF NOT EXISTS `data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(11) COLLATE utf8_spanish_ci NOT NULL,
  `text` varchar(11) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `data`
--

INSERT INTO `data` (`id`, `author`, `text`) VALUES
(1, 'Joelccc', 'OK'),
(2, 'Andres', 'Person');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext COLLATE utf8_spanish_ci,
  `object_repr` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `app_label` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=7 ;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'log entry', 'admin', 'logentry'),
(2, 'permission', 'auth', 'permission'),
(3, 'group', 'auth', 'group'),
(4, 'user', 'auth', 'user'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=7 ;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2015-10-06 22:26:11'),
(2, 'auth', '0001_initial', '2015-10-06 22:26:14'),
(3, 'admin', '0001_initial', '2015-10-06 22:26:15'),
(4, 'sessions', '0001_initial', '2015-10-06 22:26:16'),
(5, 'PeruCall', '0001_initial', '2015-11-23 21:28:41'),
(6, 'PeruCall', '0002_auto_20151105_1501', '2015-11-23 21:28:41');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `session_data` longtext COLLATE utf8_spanish_ci NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0mpstfaueiuecsg34s8kp5o6iksod3h6', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-25 19:02:55'),
('29j8yl4md6ft0etgq91ovcv88zfyout8', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-10-21 19:18:30'),
('2g2g46h1jzmxqcx5hikpleo6vwbdyz59', 'ZWQzNTY4Zjk4ODk0ZTA1MWI5NTY5OGUzNzgwYTlhYWU0YzI1ZGUwMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQwNWM3ZDRiMGU3ZGE5ZTk2MzgxOWY1ODFmNjFiMTYzOGIxZDQwNjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjl9', '2015-11-21 21:53:42'),
('5qol3f4na76wva2bpsocpfc8gk5d75y8', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 14:55:03'),
('610gfxxb6siwf1al8mepb8trvj78lh6k', 'YjFhMTZjYjRiOTc5NWI1MWNjYTA0NmNjNmMzZGFjZGUzMDNkOTk3ODp7Il9hdXRoX3VzZXJfaGFzaCI6ImY3MzAzN2I3NWI3NjdjZGRiY2FkNmY1NDIyZjZmMTA0ZGNiZDc0Y2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjg3fQ==', '2015-12-06 02:44:58'),
('67ct0ugg1zawi1nux9sbeyin1yq4ysvq', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-12-02 23:24:58'),
('6wufkjqmi0mwqxsyfirzielfuc9cs6xy', 'ZThkZjQ3ZmFjZDA3ZjU0YjAzOWU5YzI1YWVhYmYzZmZlODQzNDU1Yjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MTB9', '2015-11-20 23:25:11'),
('7yxvdyutyeibwimhywt9fqxjqehmqrz0', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-25 19:19:03'),
('7zcwkcrr4dw05qjwbeova31rfzijp8s8', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-18 23:24:06'),
('866urwb5ffkhuikqk94hxm4lmh1jdh2a', 'NTJhMTE5YjNlMGJjZDhlZDM2MzRmNDg1ZDU3NmM0NTc0MDc5MDMyYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZWVjNWUxMTA2M2YwMWMzYjlkMmM5NzEyNWMzNWFiZDhmOWY3OTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-17 21:52:01'),
('8kv11mw5azdgrhohuefcpd77ah2g6xwh', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-13 23:52:52'),
('8l9dvflerje4xpz7xutugza5m3qjbd0i', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-26 01:50:03'),
('8n8hpwtf6ct8wuiznrgd0szvhvcpiuwe', 'MjU2NjdhMmFiM2ZhM2Q2ZDkzMTRhMmQzMDRhMmE3MDIzNzJkM2M4MDp7Il9hdXRoX3VzZXJfaGFzaCI6ImM0OGI5MTQxZDY3YmJiOWVlOGNlNzEzZDhjM2JjMDM0YTFkMzY3M2MiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjEwfQ==', '2015-11-19 00:29:32'),
('8z8nn1n3jl2vvq6oaumykgs8ip11s6y6', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 14:55:03'),
('921lcob7h4kez4w2gi7yimvb9ub7w7ux', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-16 14:29:34'),
('9f9km568gfl295wio2su96y9vzipghxe', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-18 21:26:18'),
('9s9fk1xv4bgxnp7lyd5ffqjtfz9stmut', 'OWNiMjczZWNkNDRhOGUxM2Y2NDIxYzhhMjVkNzk4NzQwOGNlYjRiMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NGMwMmEzOWQ3ZjY3ZTNhMGVkNjYxYWM1Y2VjNDYyNGUwMzFiZjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjg2fQ==', '2015-12-11 15:04:59'),
('a04im99fvwywnbrgz16bu1d43e9bfk18', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-26 14:29:13'),
('aq80pqdtc0ntp99v5vme1ydci1u7rmc6', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 14:55:03'),
('ar4nuhbqhnd607ay9wpmcjgcbd7vy2n0', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-18 23:57:09'),
('b4m1t50g4zbm5lr42wkt6c3c2dk6e3ra', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-30 16:43:31'),
('b9e0x6ignp8sscxp7562oi3f448hqbpg', 'YjNiOWE5ODA0OTIwZDA0YmI5NGE5MWY5OTUxZTUzZTczNmEzN2VjNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjczYTM3MDIxMmMxZjZmNTZhMjI2ZmIzMzEwMDg2OTI0MWEyNzBhNzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjEwfQ==', '2015-11-26 19:44:06'),
('bvni428qke6en6tn9dstx6j9alzv5l1q', 'ZWQzNTY4Zjk4ODk0ZTA1MWI5NTY5OGUzNzgwYTlhYWU0YzI1ZGUwMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQwNWM3ZDRiMGU3ZGE5ZTk2MzgxOWY1ODFmNjFiMTYzOGIxZDQwNjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjl9', '2015-12-02 20:19:57'),
('chc6m6r64vo4ip9ck02zvlux41pxwp4q', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-27 18:04:59'),
('d1alhesy57y8clnss7smc47yoni6rqvg', 'NTJhMTE5YjNlMGJjZDhlZDM2MzRmNDg1ZDU3NmM0NTc0MDc5MDMyYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImNhZWVjNWUxMTA2M2YwMWMzYjlkMmM5NzEyNWMzNWFiZDhmOWY3OTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-14 17:47:20'),
('d8s5co329ylugpkfja237g5je054577v', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-22 16:31:20'),
('f6ad8xoo5ctu5q42bmj2weovo8vpi9e3', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-27 19:01:15'),
('flkfkduskoxykx4l579ysmsu4afbymdu', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 15:16:29'),
('fmfq6h5vxdbjnuctrvpnpv516krw4qqo', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-19 01:44:40'),
('fnq6rzq1jcgtoqteahug71eis7mj82js', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-12-02 23:14:17'),
('ftyiqyare2p6g6yrewk4dz7e21c7prxt', 'MjlmYzc4Y2Q5N2E5Njk0YjU4NzkzMjI5ZmFkYjkzNTEyMWRlNGU3NDp7Il9hdXRoX3VzZXJfaGFzaCI6ImNjMTk5MzFmZDRlNDQ1YzNiNDAyMGFlOWY2YjFjMTlmZjViNzI0YmQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-10-26 15:20:38'),
('fuxm8u2rhvo4a7ciwqnumdl6c5sb2znq', 'OWNiMjczZWNkNDRhOGUxM2Y2NDIxYzhhMjVkNzk4NzQwOGNlYjRiMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjE2NGMwMmEzOWQ3ZjY3ZTNhMGVkNjYxYWM1Y2VjNDYyNGUwMzFiZjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjg2fQ==', '2015-12-06 01:48:35'),
('g7bo2aywt6ju4xb5bn0bsyyawxr7o1yd', 'ZWQzNTY4Zjk4ODk0ZTA1MWI5NTY5OGUzNzgwYTlhYWU0YzI1ZGUwMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQwNWM3ZDRiMGU3ZGE5ZTk2MzgxOWY1ODFmNjFiMTYzOGIxZDQwNjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjl9', '2015-11-17 17:36:50'),
('ghb3omhqvzez5blcqlcto24jefpxmjhe', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-10-20 23:07:19'),
('h56cb3pvbjgj2teofqlo126x9mktkihj', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-04 17:55:16'),
('ha34u7391f8pulgt7f102z3j06d5lgne', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-20 21:57:48'),
('hdmvya04tqwg8lzha1altklb6npds4x1', 'ZWQzNTY4Zjk4ODk0ZTA1MWI5NTY5OGUzNzgwYTlhYWU0YzI1ZGUwMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQwNWM3ZDRiMGU3ZGE5ZTk2MzgxOWY1ODFmNjFiMTYzOGIxZDQwNjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjl9', '2015-12-02 04:27:25'),
('hxh96ipc82us9hw17fnm6gsnkhk5i8xs', 'ZWQzNTY4Zjk4ODk0ZTA1MWI5NTY5OGUzNzgwYTlhYWU0YzI1ZGUwMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQwNWM3ZDRiMGU3ZGE5ZTk2MzgxOWY1ODFmNjFiMTYzOGIxZDQwNjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjl9', '2015-12-02 20:35:55'),
('i47wc2ky7y95j9b0em6bzwatz76c3fhf', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 14:55:03'),
('i4kx5ksiozmhlqd2cf2stdf75bngew5t', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-02 22:39:27'),
('ibl2lyke0pa9m3m4nh52nx3h8wgfyyvv', 'MTI0OWMyOTAzMTlhNTcxY2M5OWM2YjVjMWFlOThjYjc5ZTZhMDA5NTp7Il9hdXRoX3VzZXJfaGFzaCI6ImNiMjk3MzQxNDMzNjhiYWFlZDNiMDE1NjI5MzI5NGZhNDNiMTUxNTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjg5fQ==', '2015-12-09 16:47:17'),
('io6f0gw2h3cr8s73ylptln8xl2uvls4d', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-20 21:40:57'),
('iw51oo0og7php6oywp5gbcbk7u4j3iqg', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-26 17:02:07'),
('iwuxs1kjolxvhj0ytpbgvhkc0be0mo8x', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 15:16:29'),
('j47y3sofe2o6izl0kbddyjk55zruy816', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 15:16:29'),
('jdyq31ss0hdtggeqloua1j0ifhrd9cz2', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-25 19:32:25'),
('jpamjnqbvqk77fsy04pfmfb19hjfguxg', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-13 23:52:53'),
('kbgbn8es4peuess9xeosl9d4taydhpxm', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 14:55:03'),
('lznqy9l0eosbophh6vwz6o008gmhva7w', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 15:16:29'),
('n90flxfib781e8hzq9mqu0mo2i57rbwn', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-12-03 05:09:44'),
('nj2v08gxjfqiwuw6gxg0ffn5gqjbcnlq', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 15:16:29'),
('o69andh43skvc1dmyycw8qirwj4uqpyu', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-13 23:52:44'),
('o6udc4og3fgqyv3ivkfrksz2kz724j5s', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 14:55:03'),
('oplik0kaxp5bc714xq870dv86i6langb', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-12-02 16:26:44'),
('or8hee7bu4vvjodvp26wsrahzhxfz2gn', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-12-03 16:10:52'),
('p0vyzdnq7zd6tg3nw21ilyimsr28c49m', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-14 00:43:11'),
('paiq90d4eataknkudduyx0qmf6rjdbuh', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-12-02 22:28:24'),
('phmqbr6gstsveyzl7ki2gbwz7d13rcq3', 'NTljMzVkOTBlNjc3NTEwZTljOTkyODdlMzM5NmMxZTcxZmU4ZDYxZjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2015-11-10 20:54:01'),
('ponbr70p8hposos6utkjp2n7eihndab9', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-12-03 18:27:56'),
('pq74gxddamen867fqd620wfo36euqn59', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-03 14:53:03'),
('ptn3axpvneb3y5n9j08gumwim5woz11q', 'ODU0NmU4NjA3ZjdmZDkxMGNhNTU3YTc2OWNhYjYyNGRjMjRjNDg1Yjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6N30=', '2015-11-20 23:28:48'),
('s64p635q7z2gzidegc8h2eduee2hhfg4', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-19 01:38:30'),
('s6jkh3rv1rll0pjikl29jz889cfkh5an', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-12-02 18:34:42'),
('s7wrdzvfs080czi4bjsw5ezbruymjwyj', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-14 00:06:24'),
('su04hyo0w34aqdntjfz2nougi3by0qpm', 'YjFhMTZjYjRiOTc5NWI1MWNjYTA0NmNjNmMzZGFjZGUzMDNkOTk3ODp7Il9hdXRoX3VzZXJfaGFzaCI6ImY3MzAzN2I3NWI3NjdjZGRiY2FkNmY1NDIyZjZmMTA0ZGNiZDc0Y2YiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjg3fQ==', '2015-12-11 22:26:24'),
('t6kr739l45uoh4dxtc6459vjkdcydhpv', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-05 20:43:43'),
('tgu2qjv8y99iyyylo1mnp18hlri2nfo8', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-21 19:21:47'),
('thkitz875pc9sxfppgiyrs5vn6u399s3', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-27 02:27:44'),
('trelgsy5mfm2439furc0awvn0mpfeibh', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-25 04:31:02'),
('tu49ah3nzg7hxftt5wjnbs4lx8xalvy6', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-11-18 00:11:27'),
('u58nkm4l9gwoghrd4aorlw2eb6o8q2hp', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-12-02 20:23:56'),
('vgommx2wf9igvpt53ms11d12nir0o9km', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-10-26 16:45:45'),
('vi0n0cdkucww8ibjgwlp3xgqrtxbe3hw', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-20 21:50:18'),
('vx7a2324fhafhulg5o1mj0dfylel3q9y', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 14:55:03'),
('w3saec9y3q14rypygcxk3dew5m2vposy', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 14:55:03'),
('w5npffosc39o7gvng0p67bqzrntxmgrv', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-27 01:24:15'),
('wb55katxsmqxc11igh2p9u7neax8mtlp', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-24 16:56:41'),
('wuej0egr7lcbal884aazivnwtxyz9xft', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-25 19:36:37'),
('x8ebvg2o80h6r7vjm7x89hxc6vp3z544', 'ZWQzNTY4Zjk4ODk0ZTA1MWI5NTY5OGUzNzgwYTlhYWU0YzI1ZGUwMjp7Il9hdXRoX3VzZXJfaGFzaCI6ImQwNWM3ZDRiMGU3ZGE5ZTk2MzgxOWY1ODFmNjFiMTYzOGIxZDQwNjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjl9', '2015-11-20 18:57:08'),
('xrgf3fx9udlu9xp3z0se7bmlqq049tro', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-20 21:51:40'),
('y1tx1w7l04yzmjznvjn1lps7phbkjwob', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 19:15:08'),
('y5wyesbjluto9cngi94hkb6xmacmpdm3', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-12-03 17:48:17'),
('yf7m55hhk3rqrupj5yl3jpco3f526abi', 'NmFmZWJlZTgwNWJhNjc5ZTYxNWEzN2ZlNDliYWVmOTJiOWQ1ODMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjZiZjEyN2YzOTQ4YThmMDY3YjE5ZjlmZGU3ODMzZjA5YTdmMDNhZjgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjh9', '2015-12-03 04:16:23'),
('yftxx5lhg2uu5anokjoe7fxddbd99k23', 'Zjg3YzUwZTk4NTgyM2JjNTc5YmVhMzA4Y2U5MDRhOGJiYjU1NWZiZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFkYmYxYmIwNmI1ZTc0ZmNiYmNkMzQxMzc2ZmM2MmViMWEzZDg0OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjd9', '2015-11-27 14:35:28'),
('z4e99tulhwq0xxi5den9m9ibekdz0qud', 'MzFjNzUwZmI2M2QzY2NjZTM4NmMzNDVkNDNmNTMwMDUwNDM5MWI2Njp7Il9hdXRoX3VzZXJfaGFzaCI6IjJlY2YyMmZiZWFlZTIzZTMyMGU3YjJmMzUxMjljMGQ2ZGU4ZjJkOTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9', '2015-10-26 16:42:03'),
('zoaaja4bffs7cukfpnl52siyxp19g60i', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-12-10 14:55:03'),
('zyu818pkxynd68s0orgi4kfbajsk544j', 'YWZlNjBiNGEwMjZmMzA4ZjBkM2MzYWE3MjJjNThlZDEwMjRmYTgxMTp7fQ==', '2015-11-19 15:35:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE IF NOT EXISTS `empresa` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `contacto` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `mail` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `licencias` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `mascaras` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` int(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=55 ;

--
-- Volcado de datos para la tabla `empresa`
--

INSERT INTO `empresa` (`id`, `nombre`, `contacto`, `mail`, `licencias`, `mascaras`, `telefono`) VALUES
(1, 'PeruCall', '', '', '', '', 0),
(2, 'Mego', '3232', '3232', '434', '323', 12121),
(3, 'PeruCall', '2121', 'joelr@neho.com', '121', '212121', 121),
(46, 'Mego1', '232', 'joel222@gmail', '1', '1222', 333),
(47, 'Unilab', '123', 'joel@gmail.com', '1', '1', 123),
(48, 'pcall', 'jnapuri', 'jnapuri@pcall.com', '30', 'Interna', 999988887),
(50, 'Princo', '13', 'joel@gmail.com', '1', '123', 1234),
(53, 'Brujitas S.A', '121', 'brujitas@gmail.com', '1', '12121', 45698697),
(54, 'Xiencias EIRL', '235235', 'admin@mail.xiencias.com', '100', '234234', 6409521);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

CREATE TABLE IF NOT EXISTS `estado` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=7 ;

--
-- Volcado de datos para la tabla `estado`
--

INSERT INTO `estado` (`id`, `nombre`) VALUES
(1, 'No Login'),
(2, 'En Espera'),
(3, 'En Llamada'),
(4, 'Descolgado'),
(5, 'En Pausa'),
(6, 'En gestion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `filtro`
--

CREATE TABLE IF NOT EXISTS `filtro` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `campania` int(100) DEFAULT NULL,
  `ciudad` varchar(1000) COLLATE utf8_spanish_ci DEFAULT NULL,
  `segmento` varchar(1000) COLLATE utf8_spanish_ci DEFAULT NULL,
  `grupo` varchar(1000) COLLATE utf8_spanish_ci DEFAULT NULL,
  `resultado` varchar(1000) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `campania` (`campania`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=55 ;

--
-- Volcado de datos para la tabla `filtro`
--

INSERT INTO `filtro` (`id`, `campania`, `ciudad`, `segmento`, `grupo`, `resultado`) VALUES
(31, 9, 'Arequipa/Ayacucho/', 'Indirecto/', 'Score B/', 'Contacto sin promesa/Dificultad de pago/'),
(32, 8, 'AYACUCHO/LIMA/', 'u''SCORE A''/u''SCORE C''/', 'NUEVO/INDIRECTO/', 'Contacto sin promesa/Dificultad de pago/'),
(33, 8, 'AYACUCHO/LIMA/u''AREQUIPA''/', 'SCORE C/u''SCORE A''/', 'DIRECTO/NUEVO/INDIRECTO/u''DIRECTO''/', 'Contacto sin promesa/Dificultad de pago/'),
(34, 8, 'LIMA/u''AREQUIPA''/u''AYACUCHO''/', 'u''SCORE A''/', 'NUEVO/', 'Contacto sin promesa/Dificultad de pago/'),
(35, 8, 'AYACUCHO/LIMA/', 'u''SCORE A''/', 'DIRECTO/', 'Contacto sin promesa/Dificultad de pago/'),
(36, 8, 'AYACUCHO/', 'u''SCORE A''/', 'DIRECTO/', 'Contacto sin promesa/Dificultad de pago/'),
(37, 8, 'LIMA/', 'SCORE C/', 'NUEVO/', 'Contacto sin promesa/Dificultad de pago/'),
(38, 8, 'LIMA/', 'SCORE C/', 'DIRECTO/', 'Contacto sin promesa/Dificultad de pago/'),
(41, 8, 'u''AREQUIPA''/', 'u''SCORE A''/', 'NUEVO/', 'Contacto sin promesa/Dificultad de pago/'),
(43, 8, 'LIMA/', 'u''SCORE A''/', 'INDIRECTO/', 'Contacto sin promesa/Dificultad de pago/'),
(45, 8, 'AYACUCHO/', 'u''SCORE A''/', 'NUEVO/INDIRECTO/u''DIRECTO''/', 'Fallecido/'),
(46, 60, 'AYACUCHO/LIMA/', 'SCORE C/', 'DIRECTO/', 'Fallecido/'),
(47, 61, 'AYACUCHO/', 'SCORE C/', 'INDIRECTO/', 'Fallecido/Consulta en tramite/Contacto sin promesa/Dificultad de pago/Acuerdo con fecha de pago/Reclamo Institucion/'),
(48, 61, 'AYACUCHO/', 'SCORE A/', 'INDIRECTO/', 'Fallecido/Consulta en tramite/Contacto sin promesa/'),
(49, 61, 'AREQUIPA/AYACUCHO/LIMA/', 'SCORE A/SCORE C/SCORE B/', 'DIRECTO/INDIRECTO/NUEVO/', 'Fallecido/Consulta en tramite/Contacto sin promesa/Dificultad de pago/Acuerdo con fecha de pago/Reclamo Institucion/'),
(50, 61, 'AREQUIPA/AYACUCHO/LIMA/', 'SCORE A/SCORE C/SCORE B/', 'DIRECTO/INDIRECTO/NUEVO/', 'Nuevo/'),
(51, 63, 'AREQUIPA/AYACUCHO/LIMA/', 'SCORE A/SCORE C/SCORE B/', 'DIRECTO/INDIRECTO/NUEVO/', 'Nuevo/'),
(52, 63, 'AYACUCHO/', 'SCORE A/', 'DIRECTO/INDIRECTO/', 'Nuevo/'),
(53, 63, 'AREQUIPA/AYACUCHO/LIMA/', 'SCORE A/SCORE C/SCORE B/', 'DIRECTO/INDIRECTO/NUEVO/', 'Nuevo/'),
(54, 8, 'u''AREQUIPA''/', 'SCORE C/', 'DIRECTO/', 'Nuevo/Reclamo Institucion/Acuerdo con fecha de pago/');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel`
--

CREATE TABLE IF NOT EXISTS `nivel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=5 ;

--
-- Volcado de datos para la tabla `nivel`
--

INSERT INTO `nivel` (`id`, `nombre`) VALUES
(1, 'Administrador'),
(2, 'Supervisor'),
(3, 'Agente'),
(4, 'Manager');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resultado`
--

CREATE TABLE IF NOT EXISTS `resultado` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `codigo` varchar(100) DEFAULT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Volcado de datos para la tabla `resultado`
--

INSERT INTO `resultado` (`id`, `name`, `codigo`, `tipo`) VALUES
(1, 'Fallecido', 'BA', 'GNU'),
(2, 'Consulta en tramite', NULL, NULL),
(3, 'Contacto sin promesa', NULL, NULL),
(4, 'Dificultad de pago', NULL, NULL),
(5, 'Acuerdo con fecha de pago', NULL, NULL),
(6, 'Reclamo Institucion', NULL, NULL),
(7, 'Nuevo', NULL, NULL),
(8, 'Refinancia/Convenio', 'DI', NULL),
(9, 'Renuente/Rehuye', 'DI', NULL),
(10, 'Ya pago con boucher', 'DI', NULL),
(11, 'Tit.desconocido/ Mudado', 'IL', NULL),
(12, 'Msj Tercero(No vive/labora)', 'IN', NULL),
(13, 'Msj Tercero(Si vive/labora)', 'IN', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `supervisor`
--

CREATE TABLE IF NOT EXISTS `supervisor` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `user` int(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user` (`user`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=33 ;

--
-- Volcado de datos para la tabla `supervisor`
--

INSERT INTO `supervisor` (`id`, `user`) VALUES
(27, 87),
(28, 91),
(29, 92),
(30, 93),
(31, 94),
(32, 95);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `supervisorcartera`
--

CREATE TABLE IF NOT EXISTS `supervisorcartera` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `cartera` int(100) NOT NULL,
  `supervisor` int(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cartera` (`cartera`),
  KEY `supervisor` (`supervisor`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=90 ;

--
-- Volcado de datos para la tabla `supervisorcartera`
--

INSERT INTO `supervisorcartera` (`id`, `cartera`, `supervisor`) VALUES
(81, 20, 27),
(82, 19, 27),
(83, 20, 28),
(84, 22, 32),
(85, 21, 32),
(86, 20, 32),
(87, 19, 32),
(88, 22, 30),
(89, 21, 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `troncales`
--

CREATE TABLE IF NOT EXISTS `troncales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=3 ;

--
-- Volcado de datos para la tabla `troncales`
--

INSERT INTO `troncales` (`id`, `nombre`) VALUES
(1, 'People'),
(2, 'ThinIP');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `troncalesagentes`
--

CREATE TABLE IF NOT EXISTS `troncalesagentes` (
  `id` int(100) NOT NULL,
  `empresa` int(100) NOT NULL,
  `troncal` int(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `empresa` (`empresa`),
  KEY `troncal` (`troncal`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `agentebase`
--
ALTER TABLE `agentebase`
  ADD CONSTRAINT `agentebase_ibfk_3` FOREIGN KEY (`status`) REFERENCES `estado` (`id`),
  ADD CONSTRAINT `agentebase_ibfk_1` FOREIGN KEY (`agente`) REFERENCES `agentes` (`id`),
  ADD CONSTRAINT `agentebase_ibfk_2` FOREIGN KEY (`base`) REFERENCES `base` (`id`);

--
-- Filtros para la tabla `agentes`
--
ALTER TABLE `agentes`
  ADD CONSTRAINT `agentes_ibfk_1` FOREIGN KEY (`user`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `agentes_ibfk_3` FOREIGN KEY (`estado`) REFERENCES `estado` (`id`),
  ADD CONSTRAINT `agentes_ibfk_4` FOREIGN KEY (`supervisor`) REFERENCES `supervisor` (`id`),
  ADD CONSTRAINT `agentes_ibfk_5` FOREIGN KEY (`calificacion`) REFERENCES `base` (`id`);

--
-- Filtros para la tabla `agentescampanias`
--
ALTER TABLE `agentescampanias`
  ADD CONSTRAINT `agentescampanias_ibfk_1` FOREIGN KEY (`agente`) REFERENCES `agentes` (`id`),
  ADD CONSTRAINT `agentescampanias_ibfk_2` FOREIGN KEY (`campania`) REFERENCES `campania` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD CONSTRAINT `auth_user_ibfk_1` FOREIGN KEY (`empresa`) REFERENCES `empresa` (`id`),
  ADD CONSTRAINT `auth_user_ibfk_2` FOREIGN KEY (`nivel`) REFERENCES `nivel` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `base`
--
ALTER TABLE `base`
  ADD CONSTRAINT `base_ibfk_1` FOREIGN KEY (`campania`) REFERENCES `campania` (`id`),
  ADD CONSTRAINT `base_ibfk_2` FOREIGN KEY (`resultado`) REFERENCES `resultado` (`id`),
  ADD CONSTRAINT `base_ibfk_3` FOREIGN KEY (`agente`) REFERENCES `agentes` (`id`);

--
-- Filtros para la tabla `campania`
--
ALTER TABLE `campania`
  ADD CONSTRAINT `campania_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `campania_ibfk_2` FOREIGN KEY (`supervisor`) REFERENCES `supervisor` (`id`),
  ADD CONSTRAINT `campania_ibfk_3` FOREIGN KEY (`cartera`) REFERENCES `cartera` (`id`);

--
-- Filtros para la tabla `carteraempresa`
--
ALTER TABLE `carteraempresa`
  ADD CONSTRAINT `carteraempresa_ibfk_1` FOREIGN KEY (`cartera`) REFERENCES `cartera` (`id`),
  ADD CONSTRAINT `carteraempresa_ibfk_2` FOREIGN KEY (`empresa`) REFERENCES `empresa` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `filtro`
--
ALTER TABLE `filtro`
  ADD CONSTRAINT `filtro_ibfk_1` FOREIGN KEY (`campania`) REFERENCES `campania` (`id`);

--
-- Filtros para la tabla `supervisor`
--
ALTER TABLE `supervisor`
  ADD CONSTRAINT `supervisor_ibfk_1` FOREIGN KEY (`user`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `supervisorcartera`
--
ALTER TABLE `supervisorcartera`
  ADD CONSTRAINT `supervisorcartera_ibfk_1` FOREIGN KEY (`cartera`) REFERENCES `cartera` (`id`),
  ADD CONSTRAINT `supervisorcartera_ibfk_2` FOREIGN KEY (`supervisor`) REFERENCES `supervisor` (`id`);

--
-- Filtros para la tabla `troncalesagentes`
--
ALTER TABLE `troncalesagentes`
  ADD CONSTRAINT `troncalesagentes_ibfk_1` FOREIGN KEY (`empresa`) REFERENCES `empresa` (`id`),
  ADD CONSTRAINT `troncalesagentes_ibfk_2` FOREIGN KEY (`troncal`) REFERENCES `troncales` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
