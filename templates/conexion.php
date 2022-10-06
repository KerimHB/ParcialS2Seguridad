<?php

    $host = 'localhost';
    $port = '5432';
    $dbname = 'DarkBook';
    $user = 'postgres';
    $password = '123456';
    

    try {
        $conexion = "pgsql:host=$host;port=$port;dbname=$dbname;";
        // Requiere DSN, usuario y contraseña como parámetros
        $pdo = new PDO($conexion, $user, $password, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
    
        
    } catch (PDOException $e) {
        die($e->getMessage());
    }

    $conexion = null;
