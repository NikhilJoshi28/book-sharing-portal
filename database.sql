-- MySQL dump 10.13  Distrib 5.6.31, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: booksharing
-- ------------------------------------------------------
-- Server version	5.6.31-0ubuntu0.15.10.1

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
-- Table structure for table `bookdetails`
--

DROP TABLE IF EXISTS `bookdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookdetails` (
  `bookid` varchar(100) DEFAULT NULL,
  `bookname` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `edition` varchar(20) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `avlstatus` int(1) DEFAULT NULL,
  `userID` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookdetails`
--

LOCK TABLES `bookdetails` WRITE;
/*!40000 ALTER TABLE `bookdetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `requests` (
  `startDate` date DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  `approvalStatus` int(1) DEFAULT NULL,
  `requestID` varchar(100) DEFAULT NULL,
  `lenderID` varchar(100) DEFAULT NULL,
  `borrowerID` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userdetailes`
--

DROP TABLE IF EXISTS `userdetailes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userdetailes` (
  `uid` varchar(15) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `phoneno` bigint(12) DEFAULT NULL,
  `roomno` varchar(7) DEFAULT NULL,
  `facebookid` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userdetailes`
--

LOCK TABLES `userdetailes` WRITE;
/*!40000 ALTER TABLE `userdetailes` DISABLE KEYS */;
INSERT INTO `userdetailes` VALUES ('2015A7PS179H','Nikhil Joshi',8435122297,'S254','none'),('2015A7PS119H','Afroz Ahamad',7097727064,'S356','none'),('2015A7PS116H','Bhavesh Gawri',9133896033,'S248','none'),('2015A7PS145H','Ankit Anand',9133234361,'S251','none'),('2015A7PS121','Tilak Mundra',9133235081,'S250','none');
/*!40000 ALTER TABLE `userdetailes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `uid` varchar(15) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('2015A7PS179H','$5$rounds=535000$v8JkDtSs1yQgi8CI$HFcxycw0nLuByoDWz/b7KeNmZx3EmbDzYq6SPhWTdt7'),('2015A7PS119H','$5$rounds=535000$8El9FCeZp/gP85E9$nbdaDqhP72Nh1cWLA0FLphzN0e1WHHcvxs2tP0AjOh9'),('2015A7PS116H','$5$rounds=535000$eGjLOqyG6Yq1XRRW$60eABotCWWnV6ipk.iaZytVDuDedw9L0Ig/tGDcCvEB'),('2015A7PS145H','$5$rounds=535000$fzdrkAJ5dF3M3L4t$k8GsFnNyZTirhOzeQ4fln0PXvprl6XwVOGQbY0J2Os5'),('2015A7PS121','$5$rounds=535000$jtGiHMomhc/XyEm/$Hi8XyXcF.aPdI06KQ9sc19m4FkhLYi0v2MeYK8STH44');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-19 19:05:24
