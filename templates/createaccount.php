<html>	
	<form name ="form1" id = "1" method ="post" action ="">
		<INPUT TYPE = "TEXT" Name ="username">
		<br>
		<br>
		<INPUT TYPE = "TEXT" Name ="password">
		<INPUT TYPE = "submit" Name = "Submit" value = "Submit">
	</form>
</html>

<?PHP 
	if (isset($_POST['Submit'])) {
		$username = $_POST['username'];
		print ($username);
		print ($password);
	}
?>
