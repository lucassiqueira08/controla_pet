-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: Morumbichos
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ANIMAL`
--

DROP TABLE IF EXISTS `ANIMAL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ANIMAL` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_foto` varchar(500) DEFAULT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  `especie` varchar(50) NOT NULL,
  `raca` varchar(50) NOT NULL,
  `cor` varchar(50) DEFAULT NULL,
  `datanasc` date DEFAULT NULL,
  `observacao` varchar(200) DEFAULT NULL,
  `microchip` varchar(50) DEFAULT NULL,
  `cpf_cliente` varchar(14) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `microchip` (`microchip`),
  KEY `ANIMAL_cpf_cliente_21a45f65_fk_CLIENTE_cpf` (`cpf_cliente`),
  CONSTRAINT `ANIMAL_cpf_cliente_21a45f65_fk_CLIENTE_cpf` FOREIGN KEY (`cpf_cliente`) REFERENCES `CLIENTE` (`cpf`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ANIMAL`
--

LOCK TABLES `ANIMAL` WRITE;
/*!40000 ALTER TABLE `ANIMAL` DISABLE KEYS */;
INSERT INTO `ANIMAL` VALUES (1,NULL,'Fil','M','Ave','Spaniel Perdigueiro de Drenthe','Cinza','2015-03-06','para a editoração eletrônica, permanecendo essencialmente inalterado.','758.117.071-20','683.546.683-02'),(2,NULL,'Zeca','F','Ave','Yorkshire Terrier','Branco','2015-12-06','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','967.350.971-37','484.632.917-79'),(3,NULL,'Jujuba','F','Réptil','Spaniel Franc\\xc3\\xaas','Branco','2016-12-10','quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','945.974.789-87','472.671.233-41'),(4,NULL,'Jango','F','Felina','Galgo H\\xc3\\xbangaro','Bege','2018-08-24','Lorem Ipsum, e mais recentemente quando passou a ser','416.140.881-43','415.962.642-85'),(5,NULL,'Pipoca','F','Canina','Galgo Escoc\\xc3\\xaas','Laranja','2018-08-26','da indústria tipográfica e de impressos','604.445.331-53','239.239.939-45'),(6,NULL,'Luck','F','Ave','Pinscher Austr\\xc3\\xadaco','Bege','2016-08-13','Lorem Ipsum, e mais recentemente quando passou a ser','307.385.791-17','106.961.744-17'),(7,NULL,'Nego','M','Ave','Laika','Azul','2017-09-10','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','863.427.661-60','374.473.628-44'),(8,NULL,'Muffie','F','Réptil','Collie','Branco','2016-11-26','eletrônica como Aldus PageMaker.','800.715.689-29','386.622.330-98'),(9,NULL,'Blitz','M','Ave','Sealyham Terrier','Cinza','2018-04-27','Lorem Ipsum, e mais recentemente quando passou a ser','968.517.141-94','627.761.679-63'),(10,NULL,'Pita','M','Ave','Pequeno C\\xc3\\xa3o Le\\xc3\\xa3o','Cinza','2018-01-06','eletrônica como Aldus PageMaker.','454.944.861-11','106.961.744-17'),(11,NULL,'Bonny','F','Réptil','Collie','Laranja','2017-02-13','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','354.845.551-67','790.984.226-73'),(12,NULL,'Fofo','F','Canina','Stabyhoun','Azul','2018-02-12','integrado a softwares de editoração','478.277.734-04','665.526.612-55'),(13,NULL,'Princesa','F','Réptil','Norwich Terrier','Branco','2015-08-05','integrado a softwares de editoração','720.722.042-49','386.622.330-98'),(14,NULL,'Coldie','M','Canina','Boiadeiro Bern\\xc3\\xaas','Preto','2018-03-09','Lorem Ipsum, e mais recentemente quando passou a ser','103.362.475-93','849.887.243-90'),(15,NULL,'Ulli','F','Réptil','','Cinza','2018-12-02','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','856.813.350-88','484.632.917-79'),(16,NULL,'Cloe','F','Ave','Flat Coated Retriever','Bege','2015-10-16','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','799.924.157-53','790.984.226-73'),(17,NULL,'Pity','M','Felina','Tosa Inu','Bege','2017-07-10','eletrônica como Aldus PageMaker.','784.269.936-93','977.269.645-38'),(18,NULL,'Tobby','M','Réptil','Lulu da Pomer\\xc3\\xa2nia','Laranja','2018-01-12','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','130.852.145-22','849.887.243-90'),(19,NULL,'Teteu','M','Canina','Sabujo Franc\\xc3\\xaas','Cinza','2018-04-18','integrado a softwares de editoração','883.244.813-39','239.239.939-45'),(20,NULL,'Lali','M','Ave','','Cinza','2017-07-03','eletrônica como Aldus PageMaker.','142.403.495-81','790.984.226-73'),(21,NULL,'Amy','F','Réptil','','Laranja','2018-05-08','para a editoração eletrônica, permanecendo essencialmente inalterado.','940.646.016-71','790.984.226-73'),(22,NULL,'Gorky','F','Réptil','Dogo Argentino','Branco','2015-08-26','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','202.205.780-16','374.473.628-44'),(23,NULL,'Batata','M','Canina','Terrier Tibetano','Preto','2016-02-05','para a editoração eletrônica, permanecendo essencialmente inalterado.','603.865.690-22','415.962.642-85'),(24,NULL,'Hannah','M','Canina','Terrier Glen d\\xe2\\x80\\x99Imaal','Preto','2018-03-25','para a editoração eletrônica, permanecendo essencialmente inalterado.','549.014.208-14','829.018.414-33'),(25,NULL,'Pingo','M','Canina','Pointer','Branco','2017-03-07','e vem sendo utilizado desde o século XVI,','263.982.338-47','373.514.702-98'),(26,NULL,'Amora','F','Réptil','Bull Terrier','Branco','2018-03-07','Lorem Ipsum, e mais recentemente quando passou a ser','645.780.788-54','683.546.683-02'),(27,NULL,'Chiquita','F','Felina','Galgo das Can\\xc3\\xa1rias','Azul','2016-09-27','Lorem Ipsum é simplesmente uma simulação de texto,','174.577.310-45','849.887.243-90'),(28,NULL,'Cookie','M','Felina','Borzoi','Azul','2017-11-28','Lorem Ipsum, e mais recentemente quando passou a ser','718.016.361-17','899.326.570-73'),(29,NULL,'Jujuba','F','Réptil','','Bege','2015-06-10','eletrônica como Aldus PageMaker.','783.228.883-42','683.546.683-02'),(30,NULL,'Bolota','M','Canina','Pastor Australiano','Azul','2018-04-27','eletrônica como Aldus PageMaker.','260.159.640-28','374.473.628-44'),(31,NULL,'Ringo','M','Réptil','Bichon Fris\\xc3\\xa9','Azul','2016-02-26','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','260.500.579-51','106.961.744-17'),(32,NULL,'Harry','M','Ave','Mastim Tibetano','Cinza','2018-07-22','para fazer um livro de modelos de tipos.','312.341.041-14','435.071.486-72'),(33,NULL,'Flofy','M','Réptil','Lulu da Pomer\\xc3\\xa2nia','Branco','2018-03-24','Lorem Ipsum, e mais recentemente quando passou a ser','932.165.667-01','889.946.132-05'),(34,NULL,'Ceci','M','Canina','Pumi','Branco','2018-03-01','e vem sendo utilizado desde o século XVI,','380.375.115-28','829.018.414-33'),(35,NULL,'Teteu','M','Ave','Galgo Escoc\\xc3\\xaas','Preto','2016-03-07','e vem sendo utilizado desde o século XVI,','785.584.550-75','472.671.233-41'),(36,NULL,'','F','Réptil','Kelpie Australiano','Azul','2017-05-01','Lorem Ipsum, e mais recentemente quando passou a ser','902.057.527-75','386.622.330-98'),(37,NULL,'Dufy','M','Canina','Clumer Spaniel','Branco','2018-07-23','para a editoração eletrônica, permanecendo essencialmente inalterado.','589.060.102-41','899.326.570-73'),(38,NULL,'Pingo','F','Canina','','Laranja','2017-06-16','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','416.728.936-55','239.239.939-45'),(39,NULL,'Nanico','M','Canina','Border Collie','Cinza','2015-05-27','integrado a softwares de editoração','938.332.302-20','829.018.414-33'),(40,NULL,'Jujuba','F','Ave','Pequeno C\\xc3\\xa3o Holand\\xc3\\xaas de Ca\\xc3\\xa7a','Bege','2018-08-18','eletrônica como Aldus PageMaker.','844.207.750-83','627.761.679-63'),(41,NULL,'Ninja','M','Canina','Mastim Napolitano','Cinza','2017-08-06','da indústria tipográfica e de impressos','108.009.134-34','665.526.612-55'),(42,NULL,'Chipie','M','Ave','Bichon Havan\\xc3\\xaas','Branco','2015-02-27','para a editoração eletrônica, permanecendo essencialmente inalterado.','281.042.816-92','899.326.570-73'),(43,NULL,'Florinda','M','Réptil','Setter Irland\\xc3\\xaas','Cinza','2017-01-15','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','594.806.696-83','977.269.645-38'),(44,NULL,'Lilo','M','Ave','Flat Coated Retriever','Azul','2016-06-05','quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','647.518.086-64','627.761.679-63'),(45,NULL,'Chumbinho','F','Réptil','Grande Boiadeiro Sui\\xc3\\xa7o','Bege','2016-05-25','Lorem Ipsum, e mais recentemente quando passou a ser','506.682.397-61','899.326.570-73'),(46,NULL,'Kadu','F','Réptil','Retriever da Ba\\xc3\\xada de Chesapeake','Azul','2017-09-05','e vem sendo utilizado desde o século XVI,','963.239.053-10','106.961.744-17'),(47,NULL,'Luar','F','Ave','Eurasier','Preto','2016-07-21','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','554.548.295-27','106.961.744-17'),(48,NULL,'Julie','F','Canina','Galgo Irland\\xc3\\xaas','Azul','2016-08-04','para a editoração eletrônica, permanecendo essencialmente inalterado.','346.965.951-08','484.632.917-79'),(49,NULL,'Fada','F','Réptil','Coton de Tul\\xc3\\xa9ar','Laranja','2018-12-18','da indústria tipográfica e de impressos','355.511.974-92','386.622.330-98'),(50,NULL,'Ninja','M','Ave','Braco Dinamarqu\\xc3\\xaas','Laranja','2018-01-09','quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','749.921.557-39','415.962.642-85'),(51,NULL,'Tot\\xc3\\xb3','M','Réptil','Kishu','Cinza','2016-08-12','e vem sendo utilizado desde o século XVI,','844.281.260-22','977.269.645-38'),(52,NULL,'Biula','M','Felina','Setter Gordon','Preto','2015-01-15','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','270.411.362-96','829.018.414-33');
/*!40000 ALTER TABLE `ANIMAL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ATENDIMENTO`
--

DROP TABLE IF EXISTS `ATENDIMENTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ATENDIMENTO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `observacao` varchar(100) DEFAULT NULL,
  `data_solicitacao` datetime(6) DEFAULT NULL,
  `cpf_cliente` varchar(14) NOT NULL,
  `id_orcamento` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ATENDIMENTO_cpf_cliente_284a4fc6_fk_CLIENTE_cpf` (`cpf_cliente`),
  KEY `ATENDIMENTO_id_orcamento_f4d5fe01_fk_ORCAMENTO_id` (`id_orcamento`),
  CONSTRAINT `ATENDIMENTO_cpf_cliente_284a4fc6_fk_CLIENTE_cpf` FOREIGN KEY (`cpf_cliente`) REFERENCES `CLIENTE` (`cpf`),
  CONSTRAINT `ATENDIMENTO_id_orcamento_f4d5fe01_fk_ORCAMENTO_id` FOREIGN KEY (`id_orcamento`) REFERENCES `ORCAMENTO` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ATENDIMENTO`
--

LOCK TABLES `ATENDIMENTO` WRITE;
/*!40000 ALTER TABLE `ATENDIMENTO` DISABLE KEYS */;
INSERT INTO `ATENDIMENTO` VALUES (1,'para a editoração eletrônica, permanecendo essencialmente inalterado.','2018-02-07 00:00:00.000000','665.526.612-55',8),(2,'para fazer um livro de modelos de tipos.','2016-05-26 00:00:00.000000','665.526.612-55',20),(3,'para fazer um livro de modelos de tipos.','2018-03-11 00:00:00.000000','665.526.612-55',24),(4,'integrado a softwares de editoração','2016-06-09 00:00:00.000000','665.526.612-55',21),(5,'integrado a softwares de editoração','2018-05-20 00:00:00.000000','665.526.612-55',13),(6,'para fazer um livro de modelos de tipos.','2017-04-17 00:00:00.000000','665.526.612-55',3),(7,'Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','2018-08-11 00:00:00.000000','665.526.612-55',5),(8,'Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','2016-01-05 00:00:00.000000','665.526.612-55',17),(9,'Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','2016-04-24 00:00:00.000000','665.526.612-55',7),(10,'e vem sendo utilizado desde o século XVI,','2017-06-10 00:00:00.000000','665.526.612-55',4),(11,'para a editoração eletrônica, permanecendo essencialmente inalterado.','2016-10-01 00:00:00.000000','665.526.612-55',25),(12,'quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','2017-06-06 00:00:00.000000','665.526.612-55',20),(13,'Lorem Ipsum, e mais recentemente quando passou a ser','2017-03-23 00:00:00.000000','665.526.612-55',16),(14,'eletrônica como Aldus PageMaker.','2017-02-20 00:00:00.000000','665.526.612-55',16),(15,'e vem sendo utilizado desde o século XVI,','2016-08-21 00:00:00.000000','665.526.612-55',14),(16,'eletrônica como Aldus PageMaker.','2016-02-20 00:00:00.000000','665.526.612-55',19),(17,'quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','2016-05-09 00:00:00.000000','665.526.612-55',23),(18,'eletrônica como Aldus PageMaker.','2016-04-08 00:00:00.000000','665.526.612-55',6),(19,'Lorem Ipsum é simplesmente uma simulação de texto,','2017-06-18 00:00:00.000000','665.526.612-55',1),(20,'Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','2018-09-01 00:00:00.000000','665.526.612-55',21),(21,'quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','2015-04-22 00:00:00.000000','665.526.612-55',13),(22,'para fazer um livro de modelos de tipos.','2018-09-10 00:00:00.000000','665.526.612-55',22),(23,'integrado a softwares de editoração','2018-09-22 00:00:00.000000','665.526.612-55',2),(24,'eletrônica como Aldus PageMaker.','2018-01-07 00:00:00.000000','665.526.612-55',23),(25,'para a editoração eletrônica, permanecendo essencialmente inalterado.','2017-12-27 00:00:00.000000','665.526.612-55',11),(26,'Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','2016-06-15 00:00:00.000000','665.526.612-55',19),(27,'da indústria tipográfica e de impressos','2017-11-25 00:00:00.000000','665.526.612-55',24),(28,'para fazer um livro de modelos de tipos.','2018-09-11 00:00:00.000000','665.526.612-55',4),(29,'Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','2018-03-14 00:00:00.000000','665.526.612-55',10),(30,'Lorem Ipsum, e mais recentemente quando passou a ser','2016-09-14 00:00:00.000000','665.526.612-55',17);
/*!40000 ALTER TABLE `ATENDIMENTO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ATENDIMENTO_PROC_CLINICO`
--

DROP TABLE IF EXISTS `ATENDIMENTO_PROC_CLINICO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ATENDIMENTO_PROC_CLINICO` (
  `id_atendimento` int(11) NOT NULL,
  `id_proc_clinico` int(11) NOT NULL,
  PRIMARY KEY (`id_atendimento`),
  UNIQUE KEY `ATENDIMENTO_PROC_CLINICO_id_atendimento_id_proc_c_1930ab20_uniq` (`id_atendimento`,`id_proc_clinico`),
  KEY `ATENDIMENTO_PROC_CLI_id_proc_clinico_873ebc0b_fk_PROCEDIME` (`id_proc_clinico`),
  CONSTRAINT `ATENDIMENTO_PROC_CLI_id_atendimento_08e68d4a_fk_ATENDIMEN` FOREIGN KEY (`id_atendimento`) REFERENCES `ATENDIMENTO` (`id`),
  CONSTRAINT `ATENDIMENTO_PROC_CLI_id_proc_clinico_873ebc0b_fk_PROCEDIME` FOREIGN KEY (`id_proc_clinico`) REFERENCES `PROCEDIMENTO_CLINICO` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ATENDIMENTO_PROC_CLINICO`
--

LOCK TABLES `ATENDIMENTO_PROC_CLINICO` WRITE;
/*!40000 ALTER TABLE `ATENDIMENTO_PROC_CLINICO` DISABLE KEYS */;
INSERT INTO `ATENDIMENTO_PROC_CLINICO` VALUES (1,1),(2,1),(6,7),(7,9),(3,10),(8,10);
/*!40000 ALTER TABLE `ATENDIMENTO_PROC_CLINICO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ATENDIMENTO_PROC_ESTETICO`
--

DROP TABLE IF EXISTS `ATENDIMENTO_PROC_ESTETICO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ATENDIMENTO_PROC_ESTETICO` (
  `id_atendimento` int(11) NOT NULL,
  `id_proc_estetico` int(11) NOT NULL,
  PRIMARY KEY (`id_atendimento`),
  UNIQUE KEY `ATENDIMENTO_PROC_ESTETIC_id_atendimento_id_proc_e_826abcc9_uniq` (`id_atendimento`,`id_proc_estetico`),
  KEY `ATENDIMENTO_PROC_EST_id_proc_estetico_e572d687_fk_PROCEDIME` (`id_proc_estetico`),
  CONSTRAINT `ATENDIMENTO_PROC_EST_id_atendimento_248c3775_fk_ATENDIMEN` FOREIGN KEY (`id_atendimento`) REFERENCES `ATENDIMENTO` (`id`),
  CONSTRAINT `ATENDIMENTO_PROC_EST_id_proc_estetico_e572d687_fk_PROCEDIME` FOREIGN KEY (`id_proc_estetico`) REFERENCES `PROCEDIMENTO_ESTETICO` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ATENDIMENTO_PROC_ESTETICO`
--

LOCK TABLES `ATENDIMENTO_PROC_ESTETICO` WRITE;
/*!40000 ALTER TABLE `ATENDIMENTO_PROC_ESTETICO` DISABLE KEYS */;
INSERT INTO `ATENDIMENTO_PROC_ESTETICO` VALUES (3,1),(10,1),(5,4),(2,5),(7,9),(1,10),(6,10);
/*!40000 ALTER TABLE `ATENDIMENTO_PROC_ESTETICO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AUTORIZACAO`
--

DROP TABLE IF EXISTS `AUTORIZACAO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AUTORIZACAO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link_doc` varchar(255) DEFAULT NULL,
  `id_proc_clinico` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `link_doc` (`link_doc`),
  KEY `AUTORIZACAO_id_proc_clinico_3f6ef81d_fk_PROCEDIMENTO_CLINICO_id` (`id_proc_clinico`),
  CONSTRAINT `AUTORIZACAO_id_proc_clinico_3f6ef81d_fk_PROCEDIMENTO_CLINICO_id` FOREIGN KEY (`id_proc_clinico`) REFERENCES `PROCEDIMENTO_CLINICO` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AUTORIZACAO`
--

LOCK TABLES `AUTORIZACAO` WRITE;
/*!40000 ALTER TABLE `AUTORIZACAO` DISABLE KEYS */;
INSERT INTO `AUTORIZACAO` VALUES (1,'http://googledrive/VglPWq.com',1),(2,'http://googledrive/WlnIIm.com',3),(3,'http://googledrive/HevUZg.com',1),(4,'http://googledrive/QagNEp.com',1),(5,'http://googledrive/OqaJPu.com',2),(6,'http://googledrive/CkeXWd.com',3);
/*!40000 ALTER TABLE `AUTORIZACAO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CARGO`
--

DROP TABLE IF EXISTS `CARGO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CARGO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CARGO`
--

LOCK TABLES `CARGO` WRITE;
/*!40000 ALTER TABLE `CARGO` DISABLE KEYS */;
INSERT INTO `CARGO` VALUES (1,'Veterinario'),(2,'Banhista'),(3,'Tosador'),(4,'Recepcionista'),(5,'Motorista'),(6,'Caseiro');
/*!40000 ALTER TABLE `CARGO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CARGO_FUNCIONARIO`
--

DROP TABLE IF EXISTS `CARGO_FUNCIONARIO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CARGO_FUNCIONARIO` (
  `id_cargo` int(11) NOT NULL,
  `id_func` int(11) NOT NULL,
  PRIMARY KEY (`id_cargo`),
  UNIQUE KEY `CARGO_FUNCIONARIO_id_cargo_id_func_cd251c88_uniq` (`id_cargo`,`id_func`),
  KEY `CARGO_FUNCIONARIO_id_func_4c0f43df_fk_FUNCIONARIO_user_ptr_id` (`id_func`),
  CONSTRAINT `CARGO_FUNCIONARIO_id_cargo_5a304704_fk_CARGO_id` FOREIGN KEY (`id_cargo`) REFERENCES `CARGO` (`id`),
  CONSTRAINT `CARGO_FUNCIONARIO_id_func_4c0f43df_fk_FUNCIONARIO_user_ptr_id` FOREIGN KEY (`id_func`) REFERENCES `FUNCIONARIO` (`user_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CARGO_FUNCIONARIO`
--

LOCK TABLES `CARGO_FUNCIONARIO` WRITE;
/*!40000 ALTER TABLE `CARGO_FUNCIONARIO` DISABLE KEYS */;
INSERT INTO `CARGO_FUNCIONARIO` VALUES (3,5),(6,6),(4,7),(5,8);
/*!40000 ALTER TABLE `CARGO_FUNCIONARIO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CLIENTE`
--

DROP TABLE IF EXISTS `CLIENTE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CLIENTE` (
  `url_foto` varchar(500) DEFAULT NULL,
  `cpf` varchar(14) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `logradouro` varchar(50) NOT NULL,
  `bairro` varchar(50) NOT NULL,
  `cidade` varchar(50) NOT NULL,
  `cep` varchar(8) DEFAULT NULL,
  `numero` smallint(6) NOT NULL,
  `complemento` varchar(100) DEFAULT NULL,
  `id_tipo_cliente` int(11) NOT NULL,
  PRIMARY KEY (`cpf`),
  KEY `CLIENTE_id_tipo_cliente_97c6e619_fk_TIPO_CLIENTE_id` (`id_tipo_cliente`),
  CONSTRAINT `CLIENTE_id_tipo_cliente_97c6e619_fk_TIPO_CLIENTE_id` FOREIGN KEY (`id_tipo_cliente`) REFERENCES `TIPO_CLIENTE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CLIENTE`
--

LOCK TABLES `CLIENTE` WRITE;
/*!40000 ALTER TABLE `CLIENTE` DISABLE KEYS */;
INSERT INTO `CLIENTE` VALUES (NULL,'106.961.744-17','Ludmila Nascimento','ludmilanascimento@yahoo.com.br','Rua Cavalheiro Basílio Jafet','Centro','São Paulo','01022020',2054,'Proximo ao Posto',3),(NULL,'239.239.939-45','Constantino Melo','constantinomelo@yahoo.com.br','Rua Vinte e Cinco de Março, 990','Centro','São Paulo','01021902',6487,'Proximo ao Posto',2),(NULL,'373.514.702-98','Jaimerina Oliveira','jaimerinaoliveira@ig.com.br','Rua Vinte e Cinco de Março','Centro','São Paulo','01021200',4365,'Proximo ao Posto',3),(NULL,'374.473.628-44','Eneida Carlessi','eneidacarlessi@terra.com.br','Rua Doutor Itapura de Miranda','Centro','São Paulo','01022060',1471,'Proximo ao Posto',2),(NULL,'386.622.330-98','Yanna Mendonça','yannamendonca@yahoo.com.br','Rua Cavalheiro Basílio Jafet','Centro','São Paulo','01022020',4792,'Proximo ao Posto',3),(NULL,'415.962.642-85','Gabriel Fernandes','gabrielfernandes@terra.com.br','Rua Nioac','Sé','São Paulo','01020020',900,'Proximo ao Posto',3),(NULL,'435.071.486-72','Regina Crepaldi','reginacrepaldi@terra.com.br','Rua Vinte e Cinco de Março, 641','Centro','São Paulo','01021900',7761,'Proximo ao Posto',3),(NULL,'472.671.233-41','Rubens Sabine Carlessi','rubenssabinecarlessi@ig.com.br','Rua Vinte e Cinco de Março','Centro','São Paulo','01021100',5447,'Proximo ao Posto',1),(NULL,'484.632.917-79','Paulo Brunoro','paulobrunoro@hotmail.com','Rua Tabatinguera, 294','Sé','São Paulo','01020903',2463,'Proximo ao Posto',3),(NULL,'514.420.439-22','Otto Amorim','ottoamorim@yahoo.com.br','Rua Alexandria','Sé','São Paulo','01020050',919,'Proximo ao Posto',3),(NULL,'627.761.679-63','Abelardo Oliveira','abelardooliveira@hotmail.com','Rua Jorge Azem','Centro','São Paulo','01022030',6138,'Proximo ao Posto',2),(NULL,'665.526.612-55','Astrid Rezende','astridrezende@yahoo.com.br','Rua Tabatinguera','Sé','São Paulo','01020001',5526,'Proximo ao Posto',2),(NULL,'683.546.683-02','Clovis Lopes','clovislopes@ig.com.br','Rua Cavalheiro Basílio Jafet','Centro','São Paulo','01022020',2333,'Proximo ao Posto',2),(NULL,'790.984.226-73','Sidney Honorio','sidneyhonorio@terra.com.br','Rua Vinte e Cinco de Março','Centro','São Paulo','01021100',3616,'Proximo ao Posto',3),(NULL,'807.121.005-28','Plinio Lopes','pliniolopes@ig.com.br','Rua Tabatinguera','Sé','São Paulo','01020001',2829,'Proximo ao Posto',1),(NULL,'829.018.414-33','Abda Silva Santos','abdasilvasantos@bol.com.br','Rua Tabatinguera, 340','Sé','São Paulo','01020904',5704,'Proximo ao Posto',3),(NULL,'849.887.243-90','Cirilo Lopes','cirilolopes@ig.com.br','Rua Tabatinguera, 140','Sé','São Paulo','01020901',7892,'Proximo ao Posto',1),(NULL,'889.946.132-05','Barbara Alves','barbaraalves@ig.com.br','Rua Vinte e Cinco de Março','Centro','São Paulo','01021100',1577,'Proximo ao Posto',3),(NULL,'899.326.570-73','Carol Lopes','carollopes@hotmail.com','Rua Doutor Itapura de Miranda','Centro','São Paulo','01022060',6501,'Proximo ao Posto',3),(NULL,'977.269.645-38','John dos Anjos','johndosanjos@bol.com.br','Rua Frederico Alvarenga','Sé','São Paulo','01020030',7966,'Proximo ao Posto',1);
/*!40000 ALTER TABLE `CLIENTE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `COMISSAO`
--

DROP TABLE IF EXISTS `COMISSAO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `COMISSAO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `valor` decimal(10,2) NOT NULL,
  `id_atendimento` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `COMISSAO_id_atendimento_5c7f0649_fk_ATENDIMENTO_id` (`id_atendimento`),
  CONSTRAINT `COMISSAO_id_atendimento_5c7f0649_fk_ATENDIMENTO_id` FOREIGN KEY (`id_atendimento`) REFERENCES `ATENDIMENTO` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COMISSAO`
--

LOCK TABLES `COMISSAO` WRITE;
/*!40000 ALTER TABLE `COMISSAO` DISABLE KEYS */;
INSERT INTO `COMISSAO` VALUES (1,15.03,7),(2,15.49,10),(3,17.69,4),(4,12.96,4),(5,6.55,4),(6,18.45,2),(7,7.42,8),(8,10.46,9),(9,15.45,1),(10,5.45,7),(11,7.56,1),(12,14.51,6),(13,12.40,2),(14,5.56,10),(15,9.46,1),(16,12.35,3),(17,7.84,1),(18,17.37,10);
/*!40000 ALTER TABLE `COMISSAO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DIAGNOSTICO_ANIMAL`
--

DROP TABLE IF EXISTS `DIAGNOSTICO_ANIMAL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DIAGNOSTICO_ANIMAL` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(500) DEFAULT NULL,
  `booleano` int(11) DEFAULT NULL,
  `id_tipo_diagnostico` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `DIAGNOSTICO_ANIMAL_id_tipo_diagnostico_41d9d66b_fk_TIPO_DIAG` (`id_tipo_diagnostico`),
  CONSTRAINT `DIAGNOSTICO_ANIMAL_id_tipo_diagnostico_41d9d66b_fk_TIPO_DIAG` FOREIGN KEY (`id_tipo_diagnostico`) REFERENCES `TIPO_DIAGNOSTICO` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DIAGNOSTICO_ANIMAL`
--

LOCK TABLES `DIAGNOSTICO_ANIMAL` WRITE;
/*!40000 ALTER TABLE `DIAGNOSTICO_ANIMAL` DISABLE KEYS */;
INSERT INTO `DIAGNOSTICO_ANIMAL` VALUES (2,'Animal apresenta cansaço',1,1),(3,'Animal apresenta cansaço',1,3),(4,'Animal apresenta cansaço',1,2),(5,'Animal apresenta cansaço',0,4),(6,'Animal apresenta cansaço',0,2),(7,'Animal apresenta cansaço',0,3),(8,'Animal apresenta cansaço',1,1),(9,'Animal apresenta cansaço',1,3),(10,'Animal apresenta cansaço',1,3),(11,'Animal apresenta cansaço',1,1),(13,'Animal apresenta cansaço',0,4),(14,'Animal apresenta cansaço',1,2),(15,'Animal apresenta cansaço',0,4),(16,'Animal apresenta cansaço',1,4);
/*!40000 ALTER TABLE `DIAGNOSTICO_ANIMAL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ESTADIA`
--

DROP TABLE IF EXISTS `ESTADIA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ESTADIA` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `observacao` varchar(500) DEFAULT NULL,
  `data_inicio` datetime(6) NOT NULL,
  `data_fim` datetime(6) NOT NULL,
  `data_solicitacao` date NOT NULL,
  `valor_diaria` decimal(10,2) NOT NULL,
  `id_animal` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ESTADIA_id_animal_90833ee0_fk_ANIMAL_id` (`id_animal`),
  CONSTRAINT `ESTADIA_id_animal_90833ee0_fk_ANIMAL_id` FOREIGN KEY (`id_animal`) REFERENCES `ANIMAL` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ESTADIA`
--

LOCK TABLES `ESTADIA` WRITE;
/*!40000 ALTER TABLE `ESTADIA` DISABLE KEYS */;
INSERT INTO `ESTADIA` VALUES (1,'eletrônica como Aldus PageMaker.','2016-04-05 13:31:09.000000','2018-05-22 10:53:30.000000','2015-01-27',66.79,31),(2,'e vem sendo utilizado desde o século XVI,','2016-11-12 12:24:30.000000','2015-07-07 12:11:51.000000','2016-07-01',175.74,1),(3,'da indústria tipográfica e de impressos','2018-01-03 10:06:46.000000','2016-02-17 15:16:44.000000','2018-03-20',66.91,33),(4,'Lorem Ipsum, e mais recentemente quando passou a ser','2018-05-19 12:41:20.000000','2015-02-21 15:08:04.000000','2015-09-13',197.37,17),(5,'Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','2017-01-04 12:11:26.000000','2015-11-25 08:01:32.000000','2015-07-27',154.64,16),(6,'eletrônica como Aldus PageMaker.','2017-08-20 10:51:44.000000','2017-08-01 10:27:46.000000','2016-12-23',122.08,30),(7,'e vem sendo utilizado desde o século XVI,','2015-11-06 15:08:35.000000','2016-03-23 14:50:34.000000','2016-01-24',96.83,40),(8,'para fazer um livro de modelos de tipos.','2017-10-13 14:48:09.000000','2016-07-06 13:49:44.000000','2015-02-08',139.68,23),(9,'da indústria tipográfica e de impressos','2015-10-25 14:58:05.000000','2015-05-28 16:32:45.000000','2016-01-10',117.41,11),(10,'Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','2016-04-03 08:33:11.000000','2016-05-07 12:43:28.000000','2017-02-08',179.45,17);
/*!40000 ALTER TABLE `ESTADIA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EXAME`
--

DROP TABLE IF EXISTS `EXAME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EXAME` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link_doc` varchar(255) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `data_realizacao` date DEFAULT NULL,
  `id_animal` int(11) NOT NULL,
  `id_tipo_exame` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `link_doc` (`link_doc`),
  KEY `EXAME_id_animal_6cf2da99_fk_ANIMAL_id` (`id_animal`),
  KEY `EXAME_id_tipo_exame_023a61a9_fk_TIPO_EXAME_id` (`id_tipo_exame`),
  CONSTRAINT `EXAME_id_animal_6cf2da99_fk_ANIMAL_id` FOREIGN KEY (`id_animal`) REFERENCES `ANIMAL` (`id`),
  CONSTRAINT `EXAME_id_tipo_exame_023a61a9_fk_TIPO_EXAME_id` FOREIGN KEY (`id_tipo_exame`) REFERENCES `TIPO_EXAME` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EXAME`
--

LOCK TABLES `EXAME` WRITE;
/*!40000 ALTER TABLE `EXAME` DISABLE KEYS */;
INSERT INTO `EXAME` VALUES (1,'http://googledrive/KwnHZj.com','Exame de tal coisa do animal tal','2015-02-01',20,3),(2,'http://googledrive/UvaHYf.com','Exame de tal coisa do animal tal','2018-09-28',9,2),(3,'http://googledrive/JxkBKg.com','Exame de tal coisa do animal tal','2016-01-10',15,3),(4,'http://googledrive/SgzHTf.com','Exame de tal coisa do animal tal','2016-07-09',16,1),(5,'http://googledrive/NhkLBf.com','Exame de tal coisa do animal tal','2015-02-25',3,1),(6,'http://googledrive/BxdQRv.com','Exame de tal coisa do animal tal','2017-08-23',3,3),(7,'http://googledrive/HkqJFl.com','Exame de tal coisa do animal tal','2018-11-09',11,5),(8,'http://googledrive/IopFJa.com','Exame de tal coisa do animal tal','2017-09-09',3,2),(9,'http://googledrive/RswJNt.com','Exame de tal coisa do animal tal','2016-08-16',10,5);
/*!40000 ALTER TABLE `EXAME` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FEITO_POR`
--

DROP TABLE IF EXISTS `FEITO_POR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FEITO_POR` (
  `id_atendimento` int(11) NOT NULL,
  `data_realizacao` date DEFAULT NULL,
  `id_funcionario` int(11) NOT NULL,
  PRIMARY KEY (`id_atendimento`),
  UNIQUE KEY `FEITO_POR_id_atendimento_id_funcionario_4b9d9a30_uniq` (`id_atendimento`,`id_funcionario`),
  KEY `FEITO_POR_id_funcionario_64d49259_fk_FUNCIONARIO_user_ptr_id` (`id_funcionario`),
  CONSTRAINT `FEITO_POR_id_atendimento_f1798a20_fk_ATENDIMENTO_id` FOREIGN KEY (`id_atendimento`) REFERENCES `ATENDIMENTO` (`id`),
  CONSTRAINT `FEITO_POR_id_funcionario_64d49259_fk_FUNCIONARIO_user_ptr_id` FOREIGN KEY (`id_funcionario`) REFERENCES `FUNCIONARIO` (`user_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FEITO_POR`
--

LOCK TABLES `FEITO_POR` WRITE;
/*!40000 ALTER TABLE `FEITO_POR` DISABLE KEYS */;
INSERT INTO `FEITO_POR` VALUES (3,'2015-10-06',10),(4,'2017-03-05',6),(5,'2017-12-22',5),(6,'2017-04-12',8);
/*!40000 ALTER TABLE `FEITO_POR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FICHA_ANIMAL`
--

DROP TABLE IF EXISTS `FICHA_ANIMAL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FICHA_ANIMAL` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data_consulta` date NOT NULL,
  `descricao` varchar(500) DEFAULT NULL,
  `id_animal` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FICHA_ANIMAL_id_animal_87fd72f6_fk_ANIMAL_id` (`id_animal`),
  CONSTRAINT `FICHA_ANIMAL_id_animal_87fd72f6_fk_ANIMAL_id` FOREIGN KEY (`id_animal`) REFERENCES `ANIMAL` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FICHA_ANIMAL`
--

LOCK TABLES `FICHA_ANIMAL` WRITE;
/*!40000 ALTER TABLE `FICHA_ANIMAL` DISABLE KEYS */;
INSERT INTO `FICHA_ANIMAL` VALUES (1,'2015-12-04','e vem sendo utilizado desde o século XVI,',17),(2,'2016-10-16','integrado a softwares de editoração',11),(3,'2017-08-18','quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou',15),(4,'2017-01-28','para fazer um livro de modelos de tipos.',16),(5,'2018-12-15','da indústria tipográfica e de impressos',5),(6,'2017-04-23','Lorem Ipsum é simplesmente uma simulação de texto,',13),(7,'2017-10-28','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de',3),(8,'2017-05-16','Lorem Ipsum é simplesmente uma simulação de texto,',14),(9,'2018-10-05','para a editoração eletrônica, permanecendo essencialmente inalterado.',9),(10,'2015-01-19','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto',9),(11,'2015-12-05','eletrônica como Aldus PageMaker.',2),(12,'2015-05-28','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de',2),(13,'2018-02-28','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de',1),(14,'2017-01-07','Lorem Ipsum, e mais recentemente quando passou a ser',18),(15,'2016-09-23','e vem sendo utilizado desde o século XVI,',2),(16,'2015-12-10','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto',12),(17,'2016-02-11','Lorem Ipsum é simplesmente uma simulação de texto,',15),(18,'2018-06-14','para a editoração eletrônica, permanecendo essencialmente inalterado.',9),(19,'2017-10-18','Lorem Ipsum é simplesmente uma simulação de texto,',12),(20,'2018-05-23','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de',6);
/*!40000 ALTER TABLE `FICHA_ANIMAL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FICHA_DIAGNOSTICO`
--

DROP TABLE IF EXISTS `FICHA_DIAGNOSTICO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FICHA_DIAGNOSTICO` (
  `id_diagnostico` int(11) NOT NULL,
  `id_ficha` int(11) NOT NULL,
  PRIMARY KEY (`id_diagnostico`),
  UNIQUE KEY `FICHA_DIAGNOSTICO_id_diagnostico_id_ficha_fb8be9a6_uniq` (`id_diagnostico`,`id_ficha`),
  KEY `FICHA_DIAGNOSTICO_id_ficha_fb2e7934_fk_FICHA_ANIMAL_id` (`id_ficha`),
  CONSTRAINT `FICHA_DIAGNOSTICO_id_diagnostico_951ce7b9_fk_DIAGNOSTI` FOREIGN KEY (`id_diagnostico`) REFERENCES `DIAGNOSTICO_ANIMAL` (`id`),
  CONSTRAINT `FICHA_DIAGNOSTICO_id_ficha_fb2e7934_fk_FICHA_ANIMAL_id` FOREIGN KEY (`id_ficha`) REFERENCES `FICHA_ANIMAL` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FICHA_DIAGNOSTICO`
--

LOCK TABLES `FICHA_DIAGNOSTICO` WRITE;
/*!40000 ALTER TABLE `FICHA_DIAGNOSTICO` DISABLE KEYS */;
INSERT INTO `FICHA_DIAGNOSTICO` VALUES (2,2),(5,2),(3,4);
/*!40000 ALTER TABLE `FICHA_DIAGNOSTICO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FUNCIONARIO`
--

DROP TABLE IF EXISTS `FUNCIONARIO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FUNCIONARIO` (
  `user_ptr_id` int(11) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `data_nasc` date NOT NULL,
  `equipe_sistema` tinyint(1) NOT NULL,
  `apelido` varchar(30) NOT NULL,
  `situacao_func` varchar(30) NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  UNIQUE KEY `cpf` (`cpf`),
  CONSTRAINT `FUNCIONARIO_user_ptr_id_8a773a54_fk_USER_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `USER` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FUNCIONARIO`
--

LOCK TABLES `FUNCIONARIO` WRITE;
/*!40000 ALTER TABLE `FUNCIONARIO` DISABLE KEYS */;
INSERT INTO `FUNCIONARIO` VALUES (4,'175.742.742-39','2018-12-26',1,'','Ativo'),(5,'894.670.075-65','2017-12-20',1,'','Ativo'),(6,'204.365.089-94','2016-07-15',1,'','Ativo'),(7,'189.752.846-07','2015-05-14',1,'','Inativo'),(8,'409.721.570-67','2015-06-01',1,'','Ativo'),(10,'717.019.671-45','2015-07-14',0,'','Inativo');
/*!40000 ALTER TABLE `FUNCIONARIO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ORCAMENTO`
--

DROP TABLE IF EXISTS `ORCAMENTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ORCAMENTO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `preco_final` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=115 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ORCAMENTO`
--

LOCK TABLES `ORCAMENTO` WRITE;
/*!40000 ALTER TABLE `ORCAMENTO` DISABLE KEYS */;
INSERT INTO `ORCAMENTO` VALUES (1,50.00),(2,25.00),(3,35.00),(4,50.00),(5,25.00),(6,35.00),(7,50.00),(8,25.00),(9,35.00),(10,50.00),(11,25.00),(12,35.00),(13,50.00),(14,25.00),(15,35.00),(16,50.00),(17,25.00),(18,35.00),(19,50.00),(20,25.00),(21,35.00),(22,50.00),(23,25.00),(24,35.00),(25,50.00),(26,25.00),(27,35.00),(28,50.00),(29,25.00),(30,35.00),(31,50.00),(32,25.00),(33,35.00),(34,50.00),(35,25.00),(36,35.00),(37,50.00),(38,25.00),(39,35.00),(40,50.00),(41,25.00),(42,35.00),(43,50.00),(44,25.00),(45,35.00),(46,50.00),(47,25.00),(48,35.00),(49,50.00),(50,25.00),(51,35.00),(52,50.00),(53,25.00),(54,35.00),(55,50.00),(56,25.00),(57,35.00),(58,50.00),(59,25.00),(60,35.00),(61,50.00),(62,25.00),(63,35.00),(64,50.00),(65,25.00),(66,35.00),(67,50.00),(68,25.00),(69,35.00),(70,50.00),(71,25.00),(72,35.00),(73,50.00),(74,25.00),(75,35.00),(76,50.00),(77,25.00),(78,35.00),(79,50.00),(80,25.00),(81,35.00),(82,50.00),(83,25.00),(84,35.00),(85,50.00),(86,25.00),(87,35.00),(88,50.00),(89,25.00),(90,35.00),(91,50.00),(92,25.00),(93,35.00),(94,50.00),(95,25.00),(96,35.00),(97,50.00),(98,25.00),(99,35.00),(100,50.00),(101,25.00),(102,35.00),(103,50.00),(104,25.00),(105,35.00),(106,50.00),(107,25.00),(108,35.00),(109,50.00),(110,25.00),(111,35.00),(112,50.00),(113,25.00),(114,35.00);
/*!40000 ALTER TABLE `ORCAMENTO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROCEDIMENTO_CLINICO`
--

DROP TABLE IF EXISTS `PROCEDIMENTO_CLINICO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PROCEDIMENTO_CLINICO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(200) NOT NULL,
  `especie` varchar(50) NOT NULL,
  `preco` decimal(10,2) NOT NULL,
  `id_tipo_proc` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `PROCEDIMENTO_CLINICO_id_tipo_proc_6fbe260a_fk_TIPO_PROC` (`id_tipo_proc`),
  CONSTRAINT `PROCEDIMENTO_CLINICO_id_tipo_proc_6fbe260a_fk_TIPO_PROC` FOREIGN KEY (`id_tipo_proc`) REFERENCES `TIPO_PROCEDIMENTO` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROCEDIMENTO_CLINICO`
--

LOCK TABLES `PROCEDIMENTO_CLINICO` WRITE;
/*!40000 ALTER TABLE `PROCEDIMENTO_CLINICO` DISABLE KEYS */;
INSERT INTO `PROCEDIMENTO_CLINICO` VALUES (1,'Aplicar vacina','para a editoração eletrônica, permanecendo essencialmente inalterado.','Réptil',103.01,3),(2,'Realizar Consulta','Lorem Ipsum é simplesmente uma simulação de texto,','Réptil',174.02,1),(3,'Realizar Eutanasia','Lorem Ipsum, e mais recentemente quando passou a ser','Réptil',145.03,4),(4,'Realizar Consulta','integrado a softwares de editoração','Felina',155.97,1),(5,'Realizar Eutanasia','integrado a softwares de editoração','Felina',167.11,2),(6,'Realizar Eutanasia','para a editoração eletrônica, permanecendo essencialmente inalterado.','Réptil',141.28,5),(7,'Aplicar vacina','integrado a softwares de editoração','Felina',112.01,3),(8,'Aplicar vacina','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','Canina',59.65,1),(9,'Realizar Consulta','Lorem Ipsum é simplesmente uma simulação de texto,','Canina',60.90,2),(10,'Realizar Consulta','eletrônica como Aldus PageMaker.','Réptil',107.87,1),(11,'Realizar Consulta','quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','Réptil',100.13,5),(12,'Realizar Consulta','Lorem Ipsum, e mais recentemente quando passou a ser','Réptil',135.25,3),(13,'Aplicar vacina','eletrônica como Aldus PageMaker.','Ave',152.04,1),(14,'Aplicar vacina','para fazer um livro de modelos de tipos.','Réptil',53.32,2),(15,'Realizar Eutanasia','eletrônica como Aldus PageMaker.','Réptil',54.99,5),(16,'Realizar Eutanasia','para fazer um livro de modelos de tipos.','Canina',180.72,5),(17,'Aplicar vacina','Lorem Ipsum é simplesmente uma simulação de texto,','Réptil',135.87,2),(18,'Realizar Consulta','Lorem Ipsum, e mais recentemente quando passou a ser','Ave',184.22,2),(19,'Realizar Consulta','integrado a softwares de editoração','Réptil',69.36,1);
/*!40000 ALTER TABLE `PROCEDIMENTO_CLINICO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PROCEDIMENTO_ESTETICO`
--

DROP TABLE IF EXISTS `PROCEDIMENTO_ESTETICO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PROCEDIMENTO_ESTETICO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(200) NOT NULL,
  `especie` varchar(50) NOT NULL,
  `preco` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PROCEDIMENTO_ESTETICO`
--

LOCK TABLES `PROCEDIMENTO_ESTETICO` WRITE;
/*!40000 ALTER TABLE `PROCEDIMENTO_ESTETICO` DISABLE KEYS */;
INSERT INTO `PROCEDIMENTO_ESTETICO` VALUES (1,'Tosa Higienica','Lorem Ipsum é simplesmente uma simulação de texto,','Réptil',184.46),(2,'Tosa na Tesoura','e vem sendo utilizado desde o século XVI,','Ave',60.34),(3,'Transporte','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','Réptil',68.28),(4,'Banho','quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','Réptil',157.82),(5,'Tosa Higienica','eletrônica como Aldus PageMaker.','Canina',153.61),(6,'Tosa Higienica','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','Felina',107.69),(7,'Tosa na Maquina','para a editoração eletrônica, permanecendo essencialmente inalterado.','Ave',152.57),(8,'Transporte','integrado a softwares de editoração','Réptil',83.22),(9,'Tosa na Tesoura','Lorem Ipsum, e mais recentemente quando passou a ser','Ave',90.79),(10,'Tosa na Maquina','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','Réptil',170.38),(11,'Banho','integrado a softwares de editoração','Canina',180.61),(12,'Tosa na Tesoura','quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','Réptil',88.55),(13,'Banho','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','Ave',144.33),(14,'Banho','para fazer um livro de modelos de tipos.','Felina',101.22),(15,'Tosa na Tesoura','quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','Réptil',105.14),(16,'Banho','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','Canina',102.63),(17,'Banho','Lorem Ipsum, e mais recentemente quando passou a ser','Canina',64.15),(18,'Transporte','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','Ave',160.06),(19,'Tosa Higienica','para fazer um livro de modelos de tipos.','Felina',84.61);
/*!40000 ALTER TABLE `PROCEDIMENTO_ESTETICO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RESPONDE`
--

DROP TABLE IF EXISTS `RESPONDE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RESPONDE` (
  `cpf_responsavel` varchar(14) NOT NULL,
  `id_animal` int(11) NOT NULL,
  PRIMARY KEY (`cpf_responsavel`),
  UNIQUE KEY `RESPONDE_cpf_responsavel_id_animal_376c315c_uniq` (`cpf_responsavel`,`id_animal`),
  KEY `RESPONDE_id_animal_b71566aa_fk_ANIMAL_id` (`id_animal`),
  CONSTRAINT `RESPONDE_cpf_responsavel_fe589b3d_fk_RESPONSAVEL_cpf` FOREIGN KEY (`cpf_responsavel`) REFERENCES `RESPONSAVEL` (`cpf`),
  CONSTRAINT `RESPONDE_id_animal_b71566aa_fk_ANIMAL_id` FOREIGN KEY (`id_animal`) REFERENCES `ANIMAL` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RESPONDE`
--

LOCK TABLES `RESPONDE` WRITE;
/*!40000 ALTER TABLE `RESPONDE` DISABLE KEYS */;
INSERT INTO `RESPONDE` VALUES ('445.773.723-01',2),('588.631.000-10',2),('769.689.986-39',8),('182.638.715-48',9),('682.381.344-44',13),('476.294.167-08',14),('334.834.712-79',18);
/*!40000 ALTER TABLE `RESPONDE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RESPONSAVEL`
--

DROP TABLE IF EXISTS `RESPONSAVEL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RESPONSAVEL` (
  `cpf` varchar(14) NOT NULL,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RESPONSAVEL`
--

LOCK TABLES `RESPONSAVEL` WRITE;
/*!40000 ALTER TABLE `RESPONSAVEL` DISABLE KEYS */;
INSERT INTO `RESPONSAVEL` VALUES ('182.638.715-48','Danelise dos Anjos'),('334.834.712-79','Neia Fernandes'),('445.773.723-01','Cleber Melo'),('476.294.167-08','Cleopatra Nascimento'),('588.631.000-10','Barbara Anastacio'),('682.381.344-44','Glauco Macedo'),('769.689.986-39','Eugenio Ventura'),('843.332.134-39','Zozimo Crepaldi'),('937.534.659-73','James Lopes');
/*!40000 ALTER TABLE `RESPONSAVEL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STATUS_ANIMAL`
--

DROP TABLE IF EXISTS `STATUS_ANIMAL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STATUS_ANIMAL` (
  `id_status` int(11) NOT NULL,
  `id_animal` int(11) NOT NULL,
  PRIMARY KEY (`id_status`),
  UNIQUE KEY `STATUS_ANIMAL_id_status_id_animal_1dadc8ce_uniq` (`id_status`,`id_animal`),
  KEY `STATUS_ANIMAL_id_animal_8e706889_fk_ANIMAL_id` (`id_animal`),
  CONSTRAINT `STATUS_ANIMAL_id_animal_8e706889_fk_ANIMAL_id` FOREIGN KEY (`id_animal`) REFERENCES `ANIMAL` (`id`),
  CONSTRAINT `STATUS_ANIMAL_id_status_a0af9e0e_fk_TIPO_STATUS_ANIMAL_id` FOREIGN KEY (`id_status`) REFERENCES `TIPO_STATUS_ANIMAL` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STATUS_ANIMAL`
--

LOCK TABLES `STATUS_ANIMAL` WRITE;
/*!40000 ALTER TABLE `STATUS_ANIMAL` DISABLE KEYS */;
INSERT INTO `STATUS_ANIMAL` VALUES (1,1),(2,6);
/*!40000 ALTER TABLE `STATUS_ANIMAL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STATUS_ATENDIMENTO`
--

DROP TABLE IF EXISTS `STATUS_ATENDIMENTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STATUS_ATENDIMENTO` (
  `id_atendimento` int(11) NOT NULL,
  `id_status` int(11) NOT NULL,
  PRIMARY KEY (`id_atendimento`),
  UNIQUE KEY `STATUS_ATENDIMENTO_id_atendimento_id_status_6c736267_uniq` (`id_atendimento`,`id_status`),
  KEY `STATUS_ATENDIMENTO_id_status_c5ff1fe7_fk_TIPO_STAT` (`id_status`),
  CONSTRAINT `STATUS_ATENDIMENTO_id_atendimento_2bc1ec73_fk_ATENDIMENTO_id` FOREIGN KEY (`id_atendimento`) REFERENCES `ATENDIMENTO` (`id`),
  CONSTRAINT `STATUS_ATENDIMENTO_id_status_c5ff1fe7_fk_TIPO_STAT` FOREIGN KEY (`id_status`) REFERENCES `TIPO_STATUS_ATENDIMENTO` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STATUS_ATENDIMENTO`
--

LOCK TABLES `STATUS_ATENDIMENTO` WRITE;
/*!40000 ALTER TABLE `STATUS_ATENDIMENTO` DISABLE KEYS */;
INSERT INTO `STATUS_ATENDIMENTO` VALUES (3,1),(9,2),(1,3),(6,4),(7,4),(10,4),(4,5),(8,6);
/*!40000 ALTER TABLE `STATUS_ATENDIMENTO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STATUS_ESTADIA`
--

DROP TABLE IF EXISTS `STATUS_ESTADIA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STATUS_ESTADIA` (
  `id_estadia` int(11) NOT NULL,
  `id_status` int(11) NOT NULL,
  PRIMARY KEY (`id_estadia`),
  UNIQUE KEY `STATUS_ESTADIA_id_estadia_id_status_26b07b21_uniq` (`id_estadia`,`id_status`),
  KEY `STATUS_ESTADIA_id_status_f381da4e_fk_TIPO_STATUS_ESTADIA_id` (`id_status`),
  CONSTRAINT `STATUS_ESTADIA_id_estadia_b9b515a9_fk_ESTADIA_id` FOREIGN KEY (`id_estadia`) REFERENCES `ESTADIA` (`id`),
  CONSTRAINT `STATUS_ESTADIA_id_status_f381da4e_fk_TIPO_STATUS_ESTADIA_id` FOREIGN KEY (`id_status`) REFERENCES `TIPO_STATUS_ESTADIA` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STATUS_ESTADIA`
--

LOCK TABLES `STATUS_ESTADIA` WRITE;
/*!40000 ALTER TABLE `STATUS_ESTADIA` DISABLE KEYS */;
INSERT INTO `STATUS_ESTADIA` VALUES (10,1),(4,4),(5,4),(8,4),(3,5),(6,5),(9,5);
/*!40000 ALTER TABLE `STATUS_ESTADIA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TELEFONE_CLIENTE`
--

DROP TABLE IF EXISTS `TELEFONE_CLIENTE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TELEFONE_CLIENTE` (
  `cpf_cliente` varchar(14) NOT NULL,
  `telefone` varchar(11) NOT NULL,
  PRIMARY KEY (`cpf_cliente`),
  UNIQUE KEY `TELEFONE_CLIENTE_cpf_cliente_telefone_04d38f45_uniq` (`cpf_cliente`,`telefone`),
  CONSTRAINT `TELEFONE_CLIENTE_cpf_cliente_8cb59b22_fk_CLIENTE_cpf` FOREIGN KEY (`cpf_cliente`) REFERENCES `CLIENTE` (`cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TELEFONE_CLIENTE`
--

LOCK TABLES `TELEFONE_CLIENTE` WRITE;
/*!40000 ALTER TABLE `TELEFONE_CLIENTE` DISABLE KEYS */;
INSERT INTO `TELEFONE_CLIENTE` VALUES ('106.961.744-17','11939511147'),('239.239.939-45','11925899357'),('373.514.702-98','11979895966'),('374.473.628-44','11954866595'),('386.622.330-98','11939123552'),('415.962.642-85','11942253442'),('435.071.486-72','11988115975'),('472.671.233-41','11967893722'),('484.632.917-79','11967469668'),('514.420.439-22','11948614324'),('627.761.679-63','11967335411'),('665.526.612-55','11919636675'),('683.546.683-02','11911828169'),('790.984.226-73','11972287887'),('807.121.005-28','11938789588'),('829.018.414-33','11961249292'),('849.887.243-90','11938791661'),('889.946.132-05','11962974644'),('899.326.570-73','11992996886'),('977.269.645-38','11972179942');
/*!40000 ALTER TABLE `TELEFONE_CLIENTE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TIPO_CLIENTE`
--

DROP TABLE IF EXISTS `TIPO_CLIENTE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TIPO_CLIENTE` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TIPO_CLIENTE`
--

LOCK TABLES `TIPO_CLIENTE` WRITE;
/*!40000 ALTER TABLE `TIPO_CLIENTE` DISABLE KEYS */;
INSERT INTO `TIPO_CLIENTE` VALUES (1,'Mensal'),(2,'Eventual'),(3,'Pacote');
/*!40000 ALTER TABLE `TIPO_CLIENTE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TIPO_DIAGNOSTICO`
--

DROP TABLE IF EXISTS `TIPO_DIAGNOSTICO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TIPO_DIAGNOSTICO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TIPO_DIAGNOSTICO`
--

LOCK TABLES `TIPO_DIAGNOSTICO` WRITE;
/*!40000 ALTER TABLE `TIPO_DIAGNOSTICO` DISABLE KEYS */;
INSERT INTO `TIPO_DIAGNOSTICO` VALUES (1,'Sistema Nervoso'),(2,'Sistema Digestorio'),(3,'Sistema Respiratorio'),(4,'Sistema Locomotor');
/*!40000 ALTER TABLE `TIPO_DIAGNOSTICO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TIPO_EXAME`
--

DROP TABLE IF EXISTS `TIPO_EXAME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TIPO_EXAME` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TIPO_EXAME`
--

LOCK TABLES `TIPO_EXAME` WRITE;
/*!40000 ALTER TABLE `TIPO_EXAME` DISABLE KEYS */;
INSERT INTO `TIPO_EXAME` VALUES (1,'Check-up'),(2,'Exame de Sangue'),(3,'Exame Retal'),(4,'Exame de Urina'),(5,'Ultrassonografia'),(6,'Exame Oftalmologico');
/*!40000 ALTER TABLE `TIPO_EXAME` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TIPO_PROCEDIMENTO`
--

DROP TABLE IF EXISTS `TIPO_PROCEDIMENTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TIPO_PROCEDIMENTO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TIPO_PROCEDIMENTO`
--

LOCK TABLES `TIPO_PROCEDIMENTO` WRITE;
/*!40000 ALTER TABLE `TIPO_PROCEDIMENTO` DISABLE KEYS */;
INSERT INTO `TIPO_PROCEDIMENTO` VALUES (1,'Consulta'),(2,'Vacinação'),(3,'Cirurgia'),(4,'Eutanasia'),(5,'Medicação');
/*!40000 ALTER TABLE `TIPO_PROCEDIMENTO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TIPO_STATUS_ANIMAL`
--

DROP TABLE IF EXISTS `TIPO_STATUS_ANIMAL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TIPO_STATUS_ANIMAL` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TIPO_STATUS_ANIMAL`
--

LOCK TABLES `TIPO_STATUS_ANIMAL` WRITE;
/*!40000 ALTER TABLE `TIPO_STATUS_ANIMAL` DISABLE KEYS */;
INSERT INTO `TIPO_STATUS_ANIMAL` VALUES (1,'Falecido'),(2,'Vivo');
/*!40000 ALTER TABLE `TIPO_STATUS_ANIMAL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TIPO_STATUS_ATENDIMENTO`
--

DROP TABLE IF EXISTS `TIPO_STATUS_ATENDIMENTO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TIPO_STATUS_ATENDIMENTO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TIPO_STATUS_ATENDIMENTO`
--

LOCK TABLES `TIPO_STATUS_ATENDIMENTO` WRITE;
/*!40000 ALTER TABLE `TIPO_STATUS_ATENDIMENTO` DISABLE KEYS */;
INSERT INTO `TIPO_STATUS_ATENDIMENTO` VALUES (1,'Aberto'),(2,'Em Atendimento'),(3,'Em Transporte'),(4,'Aguardando Pagamento'),(5,'Finalizado'),(6,'Cancelado');
/*!40000 ALTER TABLE `TIPO_STATUS_ATENDIMENTO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TIPO_STATUS_ESTADIA`
--

DROP TABLE IF EXISTS `TIPO_STATUS_ESTADIA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TIPO_STATUS_ESTADIA` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TIPO_STATUS_ESTADIA`
--

LOCK TABLES `TIPO_STATUS_ESTADIA` WRITE;
/*!40000 ALTER TABLE `TIPO_STATUS_ESTADIA` DISABLE KEYS */;
INSERT INTO `TIPO_STATUS_ESTADIA` VALUES (1,'Agendado'),(2,'Encaminhado para banho'),(3,'Encaminhado para clinica'),(4,'Em Transporte'),(5,'Hospedado');
/*!40000 ALTER TABLE `TIPO_STATUS_ESTADIA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER`
--

DROP TABLE IF EXISTS `USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USER` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `primeiro_nome` varchar(50) NOT NULL,
  `ultimo_nome` varchar(50) NOT NULL,
  `login` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `situacao` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login` (`login`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USER`
--

LOCK TABLES `USER` WRITE;
/*!40000 ALTER TABLE `USER` DISABLE KEYS */;
INSERT INTO `USER` VALUES (1,'Teste@123#$','2018-01-05 00:00:00.000000','Urania','Amorim','Urania.Amorim',1,1,1),(2,'Teste@123#$','2016-07-05 00:00:00.000000','Louis','Felizardo','Louis.Felizardo',1,1,1),(3,'Teste@123#$','2016-02-24 00:00:00.000000','Venancio','Anastacio','Venancio.Anastacio',1,1,1),(4,'Teste@123#$','2015-09-17 00:00:00.000000','Natalia','Muniz','Natalia.Muniz',1,1,1),(5,'Teste@123#$','2016-02-02 00:00:00.000000','Pedro','Fernandes','Pedro.Fernandes',1,1,1),(6,'Teste@123#$','2017-02-25 00:00:00.000000','Celio','Novaes','Celio.Novaes',1,1,1),(7,'Teste@123#$','2016-05-17 00:00:00.000000','Morris','Mendonça','Morris.Mendonça',1,1,1),(8,'Teste@123#$','2015-06-05 00:00:00.000000','Christian','Macedo','Christian.Macedo',1,1,1),(9,'Teste@123#$','2017-09-14 00:00:00.000000','Lorena','Oliveira','Lorena.Oliveira',1,1,1),(10,'Teste@123#$','2017-04-22 00:00:00.000000','Suzete Salvador','Mendonça','Suzete Salvador.Mendonça',1,1,1),(11,'pbkdf2_sha256$100000$Ma5PEA6WzQDK$beZKS06sBnmjg1F17K/34Il1VYVn8Vs1E0Tb0/P0Q/0=','2018-10-06 23:52:07.906392','controla','pet','controla.pet',1,1,1);
/*!40000 ALTER TABLE `USER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER_groups`
--

DROP TABLE IF EXISTS `USER_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USER_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `USER_groups_user_id_group_id_a18874a6_uniq` (`user_id`,`group_id`),
  KEY `USER_groups_group_id_e62f4720_fk_auth_group_id` (`group_id`),
  CONSTRAINT `USER_groups_group_id_e62f4720_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `USER_groups_user_id_c98bc129_fk_USER_id` FOREIGN KEY (`user_id`) REFERENCES `USER` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USER_groups`
--

LOCK TABLES `USER_groups` WRITE;
/*!40000 ALTER TABLE `USER_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `USER_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER_user_permissions`
--

DROP TABLE IF EXISTS `USER_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USER_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `USER_user_permissions_user_id_permission_id_217489a1_uniq` (`user_id`,`permission_id`),
  KEY `USER_user_permission_permission_id_88c5bdfa_fk_auth_perm` (`permission_id`),
  CONSTRAINT `USER_user_permission_permission_id_88c5bdfa_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `USER_user_permissions_user_id_c8904d86_fk_USER_id` FOREIGN KEY (`user_id`) REFERENCES `USER` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USER_user_permissions`
--

LOCK TABLES `USER_user_permissions` WRITE;
/*!40000 ALTER TABLE `USER_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `USER_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VETERINARIO`
--

DROP TABLE IF EXISTS `VETERINARIO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VETERINARIO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cpf` varchar(14) NOT NULL,
  `data_nasc` date NOT NULL,
  `equipe_sistema` tinyint(1) NOT NULL,
  `primeiro_nome` varchar(50) NOT NULL,
  `ultimo_nome` varchar(50) NOT NULL,
  `crmv` varchar(50) NOT NULL,
  `estado_emissor` varchar(2) NOT NULL,
  `id_funcionario` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `crmv` (`crmv`),
  KEY `VETERINARIO_id_funcionario_3d9e35a0_fk_FUNCIONARIO_user_ptr_id` (`id_funcionario`),
  CONSTRAINT `VETERINARIO_id_funcionario_3d9e35a0_fk_FUNCIONARIO_user_ptr_id` FOREIGN KEY (`id_funcionario`) REFERENCES `FUNCIONARIO` (`user_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VETERINARIO`
--

LOCK TABLES `VETERINARIO` WRITE;
/*!40000 ALTER TABLE `VETERINARIO` DISABLE KEYS */;
INSERT INTO `VETERINARIO` VALUES (1,'548.751.080-22','2015-09-08',1,'Romeu','Nascimento','854.499.689-06','PR',8);
/*!40000 ALTER TABLE `VETERINARIO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add Usuário',6,'add_user'),(17,'Can change Usuário',6,'change_user'),(18,'Can delete Usuário',6,'delete_user'),(19,'Permissao de adminstrador',6,'Admin'),(20,'Permissao de usuario',6,'Usuario'),(21,'Can add Cargo',7,'add_cargo'),(22,'Can change Cargo',7,'change_cargo'),(23,'Can delete Cargo',7,'delete_cargo'),(24,'Can add Veterinário',8,'add_veterinario'),(25,'Can change Veterinário',8,'change_veterinario'),(26,'Can delete Veterinário',8,'delete_veterinario'),(27,'Can add Cargo do Funcionário',9,'add_cargofuncionario'),(28,'Can change Cargo do Funcionário',9,'change_cargofuncionario'),(29,'Can delete Cargo do Funcionário',9,'delete_cargofuncionario'),(30,'Can add Funcionário',10,'add_funcionario'),(31,'Can change Funcionário',10,'change_funcionario'),(32,'Can delete Funcionário',10,'delete_funcionario'),(33,'Can add Animal',11,'add_animal'),(34,'Can change Animal',11,'change_animal'),(35,'Can delete Animal',11,'delete_animal'),(36,'Can add Cliente',12,'add_cliente'),(37,'Can change Cliente',12,'change_cliente'),(38,'Can delete Cliente',12,'delete_cliente'),(39,'Can add Ficha do Animal',13,'add_fichaanimal'),(40,'Can change Ficha do Animal',13,'change_fichaanimal'),(41,'Can delete Ficha do Animal',13,'delete_fichaanimal'),(42,'Can add Responsável',14,'add_responsavel'),(43,'Can change Responsável',14,'change_responsavel'),(44,'Can delete Responsável',14,'delete_responsavel'),(45,'Can add Tipo de Cliente',15,'add_tipocliente'),(46,'Can change Tipo de Cliente',15,'change_tipocliente'),(47,'Can delete Tipo de Cliente',15,'delete_tipocliente'),(48,'Can add Tipo de Status do Animal',16,'add_tipostatusanimal'),(49,'Can change Tipo de Status do Animal',16,'change_tipostatusanimal'),(50,'Can delete Tipo de Status do Animal',16,'delete_tipostatusanimal'),(51,'Can add Responsável por Animal (Responde)',17,'add_responde'),(52,'Can change Responsável por Animal (Responde)',17,'change_responde'),(53,'Can delete Responsável por Animal (Responde)',17,'delete_responde'),(54,'Can add Status do Animal',18,'add_statusanimal'),(55,'Can change Status do Animal',18,'change_statusanimal'),(56,'Can delete Status do Animal',18,'delete_statusanimal'),(57,'Can add Telefone do Cliente',19,'add_telefonecliente'),(58,'Can change Telefone do Cliente',19,'change_telefonecliente'),(59,'Can delete Telefone do Cliente',19,'delete_telefonecliente'),(60,'Can add Item do Menu',20,'add_menu'),(61,'Can change Item do Menu',20,'change_menu'),(62,'Can delete Item do Menu',20,'delete_menu'),(63,'Can add Grupo dos Itens do Menu',21,'add_menugrupo'),(64,'Can change Grupo dos Itens do Menu',21,'change_menugrupo'),(65,'Can delete Grupo dos Itens do Menu',21,'delete_menugrupo'),(66,'Can add Atendimento',22,'add_atendimento'),(67,'Can change Atendimento',22,'change_atendimento'),(68,'Can delete Atendimento',22,'delete_atendimento'),(69,'Can add Autorização',23,'add_autorizacao'),(70,'Can change Autorização',23,'change_autorizacao'),(71,'Can delete Autorização',23,'delete_autorizacao'),(72,'Can add Comissão',24,'add_comissao'),(73,'Can change Comissão',24,'change_comissao'),(74,'Can delete Comissão',24,'delete_comissao'),(75,'Can add Diagnóstico do Animal',25,'add_diagnosticoanimal'),(76,'Can change Diagnóstico do Animal',25,'change_diagnosticoanimal'),(77,'Can delete Diagnóstico do Animal',25,'delete_diagnosticoanimal'),(78,'Can add Estadia',26,'add_estadia'),(79,'Can change Estadia',26,'change_estadia'),(80,'Can delete Estadia',26,'delete_estadia'),(81,'Can add Exame',27,'add_exame'),(82,'Can change Exame',27,'change_exame'),(83,'Can delete Exame',27,'delete_exame'),(84,'Can add Orçamento',28,'add_orcamento'),(85,'Can change Orçamento',28,'change_orcamento'),(86,'Can delete Orçamento',28,'delete_orcamento'),(87,'Can add Procedimento Clinico',29,'add_procedimentoclinico'),(88,'Can change Procedimento Clinico',29,'change_procedimentoclinico'),(89,'Can delete Procedimento Clinico',29,'delete_procedimentoclinico'),(90,'Can add Procedimento Estético',30,'add_procedimentoestetico'),(91,'Can change Procedimento Estético',30,'change_procedimentoestetico'),(92,'Can delete Procedimento Estético',30,'delete_procedimentoestetico'),(93,'Can add Tipo de Diagnóstico',31,'add_tipodiagnostico'),(94,'Can change Tipo de Diagnóstico',31,'change_tipodiagnostico'),(95,'Can delete Tipo de Diagnóstico',31,'delete_tipodiagnostico'),(96,'Can add Tipo de Exame',32,'add_tipoexame'),(97,'Can change Tipo de Exame',32,'change_tipoexame'),(98,'Can delete Tipo de Exame',32,'delete_tipoexame'),(99,'Can add Tipo de Procedimento',33,'add_tipoprocedimento'),(100,'Can change Tipo de Procedimento',33,'change_tipoprocedimento'),(101,'Can delete Tipo de Procedimento',33,'delete_tipoprocedimento'),(102,'Can add Tipo de Status do Atendimento',34,'add_tipostatusatendimento'),(103,'Can change Tipo de Status do Atendimento',34,'change_tipostatusatendimento'),(104,'Can delete Tipo de Status do Atendimento',34,'delete_tipostatusatendimento'),(105,'Can add Tipo de Status da Estadia',35,'add_tipostatusestadia'),(106,'Can change Tipo de Status da Estadia',35,'change_tipostatusestadia'),(107,'Can delete Tipo de Status da Estadia',35,'delete_tipostatusestadia'),(108,'Can add Atendimento do Procedimento Clinico',36,'add_atendimentoprocclinico'),(109,'Can change Atendimento do Procedimento Clinico',36,'change_atendimentoprocclinico'),(110,'Can delete Atendimento do Procedimento Clinico',36,'delete_atendimentoprocclinico'),(111,'Can add Atendimento do Procedimento Estético',37,'add_atendimentoprocestetico'),(112,'Can change Atendimento do Procedimento Estético',37,'change_atendimentoprocestetico'),(113,'Can delete Atendimento do Procedimento Estético',37,'delete_atendimentoprocestetico'),(114,'Can add Atendimento Feito por Funcionário (Feito Por)',38,'add_feitopor'),(115,'Can change Atendimento Feito por Funcionário (Feito Por)',38,'change_feitopor'),(116,'Can delete Atendimento Feito por Funcionário (Feito Por)',38,'delete_feitopor'),(117,'Can add Ficha de Diagnóstico',39,'add_fichadiagnostico'),(118,'Can change Ficha de Diagnóstico',39,'change_fichadiagnostico'),(119,'Can delete Ficha de Diagnóstico',39,'delete_fichadiagnostico'),(120,'Can add Status do Atendimento',40,'add_statusatendimento'),(121,'Can change Status do Atendimento',40,'change_statusatendimento'),(122,'Can delete Status do Atendimento',40,'delete_statusatendimento'),(123,'Can add Status da Estadia',41,'add_statusestadia'),(124,'Can change Status da Estadia',41,'change_statusestadia'),(125,'Can delete Status da Estadia',41,'delete_statusestadia');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_USER_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_USER_id` FOREIGN KEY (`user_id`) REFERENCES `USER` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-10-06 23:52:30.884850','10','Suzete Salvador Mendonça',2,'[]',6,11),(2,'2018-10-06 23:52:37.502869','10','Suzete Salvador Mendonça',2,'[]',6,11),(3,'2018-10-06 23:52:39.281958','10','Suzete Salvador Mendonça',2,'[]',6,11),(4,'2018-10-06 23:52:42.983047','10','Suzete Salvador Mendonça',2,'[]',6,11),(5,'2018-10-06 23:52:47.816269','10','Suzete Salvador Mendonça',2,'[]',6,11),(6,'2018-10-06 23:52:50.968918','9','Lorena Oliveira',2,'[]',6,11),(7,'2018-10-06 23:52:56.870716','8','Christian Macedo',2,'[]',6,11),(8,'2018-10-06 23:53:00.084151','7','Morris Mendonça',2,'[]',6,11),(9,'2018-10-06 23:53:05.323368','7','Morris Mendonça',2,'[]',6,11),(10,'2018-10-06 23:53:09.389227','6','Celio Novaes',2,'[]',6,11),(11,'2018-10-06 23:53:12.907596','5','Pedro Fernandes',2,'[]',6,11),(12,'2018-10-06 23:53:16.843321','5','Pedro Fernandes',2,'[]',6,11),(13,'2018-10-06 23:53:20.698407','4','Natalia Muniz',2,'[]',6,11),(14,'2018-10-06 23:53:24.372609','3','Venancio Anastacio',2,'[]',6,11),(15,'2018-10-06 23:53:28.694886','2','Louis Felizardo',2,'[]',6,11),(16,'2018-10-06 23:53:32.029509','1','Urania Amorim',2,'[]',6,11);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(11,'cliente','animal'),(12,'cliente','cliente'),(13,'cliente','fichaanimal'),(17,'cliente','responde'),(14,'cliente','responsavel'),(18,'cliente','statusanimal'),(19,'cliente','telefonecliente'),(15,'cliente','tipocliente'),(16,'cliente','tipostatusanimal'),(4,'contenttypes','contenttype'),(20,'core','menu'),(21,'core','menugrupo'),(22,'servicos','atendimento'),(36,'servicos','atendimentoprocclinico'),(37,'servicos','atendimentoprocestetico'),(23,'servicos','autorizacao'),(24,'servicos','comissao'),(25,'servicos','diagnosticoanimal'),(26,'servicos','estadia'),(27,'servicos','exame'),(38,'servicos','feitopor'),(39,'servicos','fichadiagnostico'),(28,'servicos','orcamento'),(29,'servicos','procedimentoclinico'),(30,'servicos','procedimentoestetico'),(40,'servicos','statusatendimento'),(41,'servicos','statusestadia'),(31,'servicos','tipodiagnostico'),(32,'servicos','tipoexame'),(33,'servicos','tipoprocedimento'),(34,'servicos','tipostatusatendimento'),(35,'servicos','tipostatusestadia'),(5,'sessions','session'),(7,'usuarios','cargo'),(9,'usuarios','cargofuncionario'),(10,'usuarios','funcionario'),(6,'usuarios','user'),(8,'usuarios','veterinario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-10-06 23:27:19.160082'),(2,'contenttypes','0002_remove_content_type_name','2018-10-06 23:27:20.380806'),(3,'auth','0001_initial','2018-10-06 23:27:24.501742'),(4,'auth','0002_alter_permission_name_max_length','2018-10-06 23:27:24.665896'),(5,'auth','0003_alter_user_email_max_length','2018-10-06 23:27:24.727096'),(6,'auth','0004_alter_user_username_opts','2018-10-06 23:27:24.774265'),(7,'auth','0005_alter_user_last_login_null','2018-10-06 23:27:24.814524'),(8,'auth','0006_require_contenttypes_0002','2018-10-06 23:27:24.854996'),(9,'auth','0007_alter_validators_add_error_messages','2018-10-06 23:27:24.894353'),(10,'auth','0008_alter_user_username_max_length','2018-10-06 23:27:24.951873'),(11,'auth','0009_alter_user_last_name_max_length','2018-10-06 23:27:24.993004'),(12,'usuarios','0001_initial','2018-10-06 23:27:36.174482'),(13,'admin','0001_initial','2018-10-06 23:27:38.098619'),(14,'admin','0002_logentry_remove_auto_add','2018-10-06 23:27:38.180573'),(15,'cliente','0001_initial','2018-10-06 23:27:52.575745'),(16,'core','0001_initial','2018-10-06 23:27:52.785596'),(17,'servicos','0001_initial','2018-10-06 23:28:59.421717'),(18,'servicos','0002_auto_20181005_2117','2018-10-06 23:29:12.896061'),(19,'sessions','0001_initial','2018-10-06 23:29:14.064289');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('r04w0434txkol5rnaoqax3tn0rw0qjs8','NWZjYzY2MWE2NTI1ZDViMTExYjQzYzIxMTJkYjZhYzM2OTQ0ZWVmMjp7Il9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNjYwNzMzYTk4YTRkMmNhZDJjNjE1YjdiMjdkY2EyZmI5NDE0MzQ5NSJ9','2018-10-20 23:52:07.972424');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-06 20:54:22
