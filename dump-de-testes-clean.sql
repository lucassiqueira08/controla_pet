DROP TABLE IF EXISTS `CARGO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CARGO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `CARGO` WRITE;
/*!40000 ALTER TABLE `CARGO` DISABLE KEYS */;
INSERT INTO `CARGO` VALUES (1,'Veterinario'),(2,'Banhista'),(3,'Tosador'),(4,'Recepcionista'),(5,'Motorista'),(6,'Caseiro');
/*!40000 ALTER TABLE `CARGO` ENABLE KEYS */;
UNLOCK TABLES;


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


LOCK TABLES `FUNCIONARIO` WRITE;
/*!40000 ALTER TABLE `FUNCIONARIO` DISABLE KEYS */;
INSERT INTO `FUNCIONARIO` VALUES (1,'564.851.404-73','2015-08-21',0,'','Ativo'),(2,'641.279.743-75','2017-08-01',0,'','Ativo'),(3,'588.996.291-50','2018-01-07',0,'','Inativo'),(4,'803.754.658-36','2016-01-20',0,'','Ativo'),(7,'586.282.474-94','2015-09-09',1,'','Inativo');
/*!40000 ALTER TABLE `FUNCIONARIO` ENABLE KEYS */;
UNLOCK TABLES;


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

LOCK TABLES `PROCEDIMENTO_CLINICO` WRITE;
/*!40000 ALTER TABLE `PROCEDIMENTO_CLINICO` DISABLE KEYS */;
INSERT INTO `PROCEDIMENTO_CLINICO` VALUES (1,'Realizar Consulta','Lorem Ipsum é simplesmente uma simulação de texto,','Réptil',79.71,3),(2,'Realizar Consulta','e vem sendo utilizado desde o século XVI,','Réptil',193.72,2),(3,'Realizar Eutanasia','eletrônica como Aldus PageMaker.','Ave',139.01,2),(4,'Realizar Consulta','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','Canina',79.34,1),(5,'Realizar Eutanasia','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','Ave',141.15,1),(6,'Realizar Consulta','eletrônica como Aldus PageMaker.','Canina',182.20,5),(7,'Realizar Eutanasia','Lorem Ipsum é simplesmente uma simulação de texto,','Felina',174.96,4),(8,'Realizar Consulta','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','Felina',81.28,4),(9,'Realizar Consulta','da indústria tipográfica e de impressos','Ave',162.81,2),(10,'Aplicar vacina','e vem sendo utilizado desde o século XVI,','Felina',145.86,2),(11,'Realizar Consulta','da indústria tipográfica e de impressos','Canina',82.47,1),(12,'Realizar Consulta','para a editoração eletrônica, permanecendo essencialmente inalterado.','Felina',179.05,1),(13,'Aplicar vacina','e vem sendo utilizado desde o século XVI,','Felina',54.99,5),(14,'Aplicar vacina','para fazer um livro de modelos de tipos.','Felina',64.96,5),(15,'Aplicar vacina','Lorem Ipsum é simplesmente uma simulação de texto,','Felina',84.91,5),(16,'Realizar Eutanasia','para fazer um livro de modelos de tipos.','Felina',69.89,1),(17,'Realizar Eutanasia','Lorem Ipsum, e mais recentemente quando passou a ser','Canina',59.07,3),(18,'Realizar Eutanasia','para fazer um livro de modelos de tipos.','Canina',146.87,2),(19,'Realizar Consulta','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','Canina',147.31,5);
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


LOCK TABLES `PROCEDIMENTO_ESTETICO` WRITE;
/*!40000 ALTER TABLE `PROCEDIMENTO_ESTETICO` DISABLE KEYS */;
INSERT INTO `PROCEDIMENTO_ESTETICO` VALUES (1,'Tosa na Tesoura','integrado a softwares de editoração','Ave',170.64),(2,'Tosa na Maquina','integrado a softwares de editoração','Réptil',119.09),(3,'Tosa Higienica','Lorem Ipsum é simplesmente uma simulação de texto,','Ave',100.75),(4,'Tosa na Maquina','e vem sendo utilizado desde o século XVI,','Felina',57.87),(5,'Tosa na Maquina','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','Canina',75.19),(6,'Tosa Higienica','Lorem Ipsum, e mais recentemente quando passou a ser','Ave',194.12),(7,'Tosa Higienica','da indústria tipográfica e de impressos','Ave',163.86),(8,'Banho','integrado a softwares de editoração','Canina',143.29),(9,'Transporte','integrado a softwares de editoração','Canina',115.96),(10,'Tosa Higienica','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','Felina',51.14),(11,'Tosa Higienica','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','Réptil',104.85),(12,'Tosa na Maquina','Se popularizou na década de 60, quando a Letraset lançou decalques contendo passagens de','Ave',59.33),(13,'Tosa na Maquina','para a editoração eletrônica, permanecendo essencialmente inalterado.','Felina',181.41),(14,'Transporte','Lorem Ipsum sobreviveu não só a cinco séculos, como também ao salto','Canina',134.08),(15,'Tosa na Tesoura','para a editoração eletrônica, permanecendo essencialmente inalterado.','Réptil',136.75),(16,'Transporte','quando um impressor desconhecido pegou uma bandeja de tipos e os embaralhou','Ave',195.38),(17,'Tosa Higienica','Lorem Ipsum, e mais recentemente quando passou a ser','Canina',115.31),(18,'Transporte','Lorem Ipsum é simplesmente uma simulação de texto,','Ave',79.73),(19,'Banho','Lorem Ipsum é simplesmente uma simulação de texto,','Canina',177.03);
/*!40000 ALTER TABLE `PROCEDIMENTO_ESTETICO` ENABLE KEYS */;
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

LOCK TABLES `TIPO_STATUS_ESTADIA` WRITE;
/*!40000 ALTER TABLE `TIPO_STATUS_ESTADIA` DISABLE KEYS */;
INSERT INTO `TIPO_STATUS_ESTADIA` VALUES (1,'Agendado'),(2,'Encaminhado para banho'),(3,'Encaminhado para clinica'),(4,'Em Transporte'),(5,'Hospedado');
/*!40000 ALTER TABLE `TIPO_STATUS_ESTADIA` ENABLE KEYS */;
UNLOCK TABLES;
