<?php

$ast1=exec("asterisk -rx 'core show channels' | grep 'active call'");
$ast_1=explode("active",$ast1);

$anx1=exec("asterisk -rx 'sip show peers' | grep 'UNKNOWN' | awk '{ print ($1)}'  ");

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

$ast_cpu=exec("top -bn 1 | grep asterisk | awk '{ print ($9)}'");
$astcpu=explode("COMMAND",$ast_cpu);

$ast_mem=exec("top -bn 1 | grep asterisk | awk '{ print ($10)}'");
$astmem=explode("COMMAND",$ast_mem);

$pyt_cpu=exec("top -bn 1 | grep python | awk '{ print ($9)}'");
$pytcpu=explode("COMMAND",$pyt_cpu);

$pyt_mem=exec("top -bn 1 | grep python | awk '{ print ($10)}'");
$pytmem=explode("COMMAND",$pyt_mem);

$sql_cpu=exec("top -bn 1 | grep mysql | awk '{ print ($9)}'");
$sqlcpu=explode("COMMAND",$sql_cpu);

$sql_mem=exec("top -bn 1 | grep mysql | awk '{ print ($10)}'");
$sqlmem=explode("COMMAND",$sql_mem);

echo "----------SERVIDOR DE APLICACIONES----------";
echo "\n";
echo "Llamadas Activas: ";
echo $ast_1[0];
echo "\n";
echo "--------------------\n";
echo "Anexos Desconocidos:\n ";
print_r ($anx1);
echo "\n";
echo "--------------------\n";
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
echo "--------------------\n";
echo "PROCESOS \n";
echo "Asterisk- Uso del CPU: ";
echo $astcpu[0];
echo "\n";
echo "Asterisk- Uso de la MEM: ";
echo $astmem[0];
echo "\n";
echo "Python- Uso del CPU: ";
echo $pytcpu[0];
echo "\n";
echo "Python- Uso de la MEM: ";
echo $pytmem[0];
echo "\n";
echo "Mysql- Uso del CPU: ";
echo $sqlcpu[0];
echo "\n";
echo "Mysql- Uso del MEM: ";
echo $sqlmem[0];
echo "\n";

$activeCall 	= $ast_1[0];
$dsk_use 	= $dsk_1[0];
$dsk_tot 	= $dsk_2[0];
$total_mem 	= $mem_tot[0];
$use_mem 	= $mem_use[0];
$total_swap 	= $swap_tot[0];
$use_swap 	= $swap_use[0];
$CPU 		= $cpu1[0];
$astCpuUse 	= $astcpu[0];
$astMemUse 	= $astmem[0];
$pytCpuUse 	= $pytcpu[0];
$pytMemUse 	= $pytmem[0];
$sqlCpuUse 	= $sqlcpu[0];
$sqlMemUse 	= $sqlmem[0];


#system ("curl --data \"memoriausada=$memoriausada&d_usado=$d_usado&d_disponible=$d_disponible&memoriatotal=$memoriatotal&memoriausada=$memoriausada&swaptotal=$swaptotal&swapusada=$swapusada&cpu=$cpu\" \"http://localhost:8000/cpuestado/\" >AstApp.html");

system ("curl --data \"activeCall=$activeCall&dsk_use=$dsk_use&dsk_tot=$dsk_tot&total_mem=$total_mem&use_mem=$use_mem&total_swap=$total_swap&use_swap=$use_swap&CPU=$CPU&astCpuUse=$astCpuUse&astMemUse=$astMemUse&pytCpuUse=$pytCpuUse&pytMemUse=$pytMemUse&sqlCpuUse=$sqlCpuUse&sqlMemUse=$sqlMemUse\" \"http://localhost:8000/astapp/\" >AstApp.html");

?>
