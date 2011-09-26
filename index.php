<html>
<body>
<table width="70%" align="center">
	<tr>
	<td>
	<b>Stuff 
	</b>
	</td>
	<td><?php echo "Welcome to Chinatown"; ?>
	</td>
	</tr>
</table>
<table width="70%" align="center">
	<tr>
	<td width="20%">
	<b>
	<a href="index.php">Home</a>
	<a href="index.php?page=cables">Cables</a>
	</b>
	</td>
	<td width="80%">
		<?php
		$page = $_GET['page'];
		if ($page){
			$path = "cables/".$page.".php";
			if (file_exists($path))
				include($path);
			else
				echo ("File Not found");
		}
		else{
			include('index.php');
		}
		?>
	</td>
	</tr>
</table>
</body>
</html>
