BEGIN;
CREATE TABLE `app_curso` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `nome` varchar(200) NOT NULL, `periodo` varchar(50) NOT NULL, `instituicao` varchar(200) NOT NULL);

COMMIT;
