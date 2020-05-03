<?php

$t = 100;

if ($t < 45) {
    echo "F";
}
else if($t < 65){
	echo "C";
}
else if($t < 75){
	echo "B";
}
else if($t <= 100){
	echo "A";
}
else{
	echo "Invalid";
}
?>