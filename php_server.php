<?php

$dsk_use=exec("df -h | grep /dev/ | awk '{ print ($3)}'");
$dsk_1=explode("/dev/",$dsk_use);
$dsk_disp=exec("df -h | grep /dev/ | awk '{ print ($4)}'");
$dsk_2=explode("/dev/",$dsk_disp);

$cpu=exec("top -bn 1 | grep Cpu  | awk '{ print ($2)}'");
$cpu1=explode("%",$cpu);

$mem=exec("top -bn 1 | grep Mem:  | awk '{ print ($3)}'");
$mem_tot=explode("KiB Mem:",$mem);

$meml=exec("top -bn 1 | grep Mem:  | awk '{ print ($5)}'");
$mem_use=explode("KiB Mem:",$meml);

$swap=exec("top -bn 1 | grep Swap:  | awk '{ print ($3)}'");
$swap_tot=explode("KiB Swap:",$swap);

$swapl=exec("top -bn 1 | grep Swap:  | awk '{ print ($5)}'");
$swap_use=explode("KiB Swap:",$swapl);

echo "Disk Usados: ";
echo $dsk_1[0];
echo "\n";
echo "Disk Disponible: ";
echo $dsk_2[0];
echo "\n";
echo "--------------------\n";
echo "Mem Total: ";
echo $mem_tot[0];
echo "\n";
echo "Mem Used: ";
echo $mem_use[0];
echo "\n";
echo "--------------------\n";
echo "Swap Total: ";
echo $swap_tot[0];
echo "\n";
echo "Swap Used: ";
echo $swap_use[0];
echo "\n";
echo "--------------------\n";
echo "CPU:  ";
echo $cpu1[0];
echo "\n";

$memoriausada= $dsk_1[0];
$d_usado= $dsk_2[0];
$d_disponible= $dsk_2[0];
$memoriatotal= $mem_tot[0];
$memoriausada= $mem_use[0];
$swaptotal= $swap_tot[0];
$swapusada= $swap_use[0];
$cpu= $cpu1[0];

system ("curl --data \"memoriausada=$memoriausada&d_usado=$d_usado&d_disponible=$d_disponible&memoriatotal=$memoriatotal&memoriausada=$memoriausada&swaptotal=$swaptotal&swapusada=$swapusada&cpu=$cpu\" \"http://localhost:8000/cpuestado/\" >mayra.html");
      


?>
