<?php
$request_path = explode("/", parse_url($_SERVER['REQUEST_URI'])['path']);

$title = "ラーメンこばたつ";
$desc = "バーチャルラーメン屋（VRamener）、「ラーメンこばたつ」のオフィシャルサイトです。";

switch ($request_path[1]) {
  case "":
    $title .= " - 〜高崎の中心で愛を叫ぶ〜";
    $target = "index";
    break;
  case "menu":
    $title = "メニュー | ".$title;
    $target = "menu";
    break;
  case "access":
    $title = "アクセス | ".$title;
    $target = "access";
    break;
  default:
    include "inc/404.php";
    exit;
}

include "inc/header.php";
include "inc/".$target.".php";
include "inc/footer.php";
