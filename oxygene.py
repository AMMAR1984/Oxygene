U
    �h�^L  �                   @   s:  e d k�r6ddlZe�d� ddlT dZdZdZdZej	ed	d
� e�
e� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� eed��Zed� edkr�e�d� n:edkr�e�d� n&edkr�e�d� ne�d� ed� ed� ed� eed��Zedk�r6q q �q6q dS )�__main__�    N�clear)�*z[1;32mz\[[0;33m\]aU  
      _____  __    __ __    __  _____   _____   __   _
     /  _  \ \ \  / / \ \  / / /  ___| | ____| |  \ | |
     | | | |  \ \/ /   \ \/ /  | |     | |__   |   \| |
     | | | |   }  {     \  /   | |  _  |  __|  | |\   |
     | |_| |  / /\ \    / /    | |_| | | |___  | | \  |
     \_____/ /_/  \_\  /_/     \_____/ |_____| |_|  \_|
     z
     by ammar1984
    g����MbP?)�tz	[0;33m *r   z-*********************************************z, Enter the product to add number ========> 1z, To search a product Enter the number ===> 2z, For the benefits Press number===========> 3z Enter your choice here:�   aB  clear ; echo ' Enter the product name:' ; read a ; echo ' Enter the price of the product:' ; read b ; echo ' Enter the price of the product sale:' ; read c ; d=`expr $c - $b` ; clear ; echo '*' ; echo '*' ; echo '=====>' $a' ===> Benefit :'$d ; echo '=====>'$a '===>' $b' ==>' $c' :'$d >> karim ; echo 'ghrieb='$d >> karim�   z�clear ; echo '*' ; echo '*'  ; echo '====>Enter the product you are looking for:' ; read p ; clear  ; echo '*' ; echo '*' ; grep $p karim �   zclear; grep 'ghrieb' karimz clear ; echo '*' ; echo '*' z-===>Sorry ..... your choice is wrong ..... !!z Choose No. 0 to continue ...)�__name__�os�systemZV7xStyle�cZYellow�pZggZ	AnimationZ	SlowIndexZSlowText�print�int�input�zr   � r   r   �
karim/k.py�<module>   sJ    




