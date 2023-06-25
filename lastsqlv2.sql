-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ssis_v2
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `course_code` varchar(7) NOT NULL,
  `course_name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES ('BSCE','BS Civil Engineering'),('BSCpE','BS Computer Engineering'),('BSChE','BS Chemical Engineering'),('BSCS','BS in Computer Science'),('BSMin','BS Mining'),('BSMin','BS Mining'),('BSCE','BS Civil Engineering'),('BSChE','BS Chemical Engineering'),('BAPan','BA Panitikan'),('BAPan','BA Panitikan'),('BAPan','BA Panitikan'),('BSCS','BS Computer Science'),('BSBA','BS Business Administration'),('BSCS','BS Computer Science');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `ID` varchar(100) NOT NULL,
  `name` varchar(255) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `YEAR_LEVEL` varchar(100) NOT NULL,
  `course_code` varchar(10) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES ('2018-0234','Jack Sparrow','M','4th Year','BSCS'),('2019-6354','Harrison Ford','M','1st Year','BSM'),('2020-9876','Geo Dags','M','3rd Year','BAPan'),('2021-0010','Asuka Kazama','F','2nd Year','BSCS'),('2021-0021','Andrei Dango','M','2nd Year','BSCS'),('2021-0303','Jin Kazama','M','2nd Year','BSCS'),('2021-0555','Lili Rocherfort','F','2nd Year','BSCS'),('2021-0788','Agnes Reoma','F','2nd Year','BSCS'),('2021-0995','George Daguman','M','2nd Year','BSCS'),('2021-0998','Jed Adriel ','M','2nd Year','BSCS'),('2021-1111','Ash Ketchum','M','2nd Year','BSCS'),('2021-1999','Kazumi Mishima','F','2nd Year','BAPan'),('2021-2283','Unique Salonga','M','2nd Year','BSCS'),('2021-2323','Amy Santiago','F','2nd Year','BSCS'),('2021-2333','Blaster Silonga','M','2nd Year','BSCS'),('2021-2625','Jason Mendoza','M','1st Year','BSCS'),('2021-3434','Kevin Hart','M','2nd Year','BSCS'),('2021-4545','Kazuya Mishima','M','2nd Year','BSCE'),('2021-5554','Miguel Benjamin','M','2nd Year','BSCS'),('2021-5835','Chidi Anagonye','M','2nd Year','BSCS'),('2021-6524','Terry Jeffords','M','2nd Year','BSCS'),('2021-6940','Lily Aldrin','F','2nd Year','BAPan'),('2021-7165','Ted Mosby','M','2nd Year','BSCS'),('2021-7272','Perry Platypus','F','2nd Year','BSCS'),('2021-7274','Paolo Benjamin','M','2nd Year','BSCS'),('2021-7366','Harry Styles','M','2nd Year','BSCS'),('2021-7666','Rosa Diaz','F','2nd Year','BSCS'),('2021-7714','Mark Dave Cole','M','2nd year','BSCS'),('2021-7736','Derek Jeter','M','2nd Year','BSCS'),('2021-7763','Gian Lorenzo Concepcion','M','2nd Year','BSCS'),('2021-7771','Potch Baretto','M','2nd Year','BSCS'),('2021-7811','Lady Rainacorn','F','2nd Year','BSCS'),('2021-8373','Princess Bubblegum','F','2nd Year','BSCS'),('2021-8550','Heihachi Mishima','M','2nd Year','BAPan'),('2021-8625','Barney Stinson','M','2nd Year','BSCS'),('2021-8758','Humphrey John Aninao','M','2nd Year','BSEd Bio'),('2021-8781','Killua Zoldyck','M','2nd Year','BSCS'),('2021-8811','Gon Freecs','M','2nd Year','BSCS'),('2021-8834','Rowel Gem Daguman','M','2nd Year','BSCS'),('2021-8883','Phoebe Buffay','F','2nd Year','BSCS'),('2021-8887','Linus Techtips','M','2nd Year','BSChE'),('2021-9323','Zild Benitez','M','2nd Year','BSCS'),('2021-9416','Regina Phalange','F','2nd Year','BSCS'),('2021-9732','Tahani Al Jamil','F','2nd Year','BSCS'),('2021-9987','Leroy Smith','M','2nd Year','BSCS'),('2021-9993','Pat Laseten','F','2nd Year','BSCS'),('2021-9999','Jake Peralta','M','2nd Year','BSCS'),('2023-0995','Marshall Eriksen','M','1st Year','BSCS'),('2023-1978','Kirk Calvin ','M','1st Year','BSMath');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-25 10:35:11
