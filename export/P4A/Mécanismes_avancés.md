# P4A/Mécanismes avancés

Original author: Kabai.

# Status spéciaux

Dans **P4A**, certaines attaques ont pour conséquence d'affecter
l'adversaire d'une condition particulière parmi les suivantes.

<table>
<tr>
<td style="padding:20px">
<center>

***Poison***  
  
![](/images/Poison_p4.jpg "/images/Poison_p4.jpg")

</center>

  
Le personnage subit des dégâts sur la durée jusqu'à ce que la condition
expire ou qu'il parvienne à toucher l'adversaire.

</td>
<td style="padding:20px">
<center>

***Panic***  
  
![](/images/Confuse_p4.jpg "/images/Confuse_p4.jpg")

</center>

  
Les effets des commandes de directions sont opposées ( devient , devient
, etc...). Expire après une certaine durée ou lorsque le personnage
touche l'adversaire.

</td>
</tr>
<tr>
<td style="padding:20px">
<center>

***Shock***  
  
![](/images/Shock_p4.jpg "/images/Shock_p4.jpg")

</center>

  
Le personnage est incapable de se déplacer à l'aide des directions. Les
déplacements provoqués par les boutons tels que le *hop* ou le *quick
escape* sont encore possibles. Expire après une certaine durée ou
lorsque le personnage touche l'adversaire.

</td>
<td style="padding:20px">
<center>

***Fear***  
  
![](/images/Fear_p4.jpg "/images/Fear_p4.jpg")

</center>

  
La première attaque de chaque combo subie par le personnage a la
propriété *Fatal counter*. D'autre part le personnage ne peut pas
déchoper. Expire après une certaine durée ou lorsque le personnage
touche l'adversaire.

</td>
</tr>
<tr>
<td style="padding:20px">
<center>

***Rage***  
  
![](/images/Rage_p4.jpg "/images/Rage_p4.jpg")

</center>

  
Le personnage ne peut pas bloquer. Augmente les dégâts infligés par le
personnage de 20%. Ne disparaît que au bout de la durée prévue.

</td>
<td style="padding:20px">
<center>

***Mute***  
  
![](/images/Mute_p4.jpg "/images/Mute_p4.jpg")

</center>

  
Le personnage ne peut pas invoquer son Persona : toutes les attaques
nécessitant le Persona sont inutilisables. Le burst est également
inutilisable. Expire après une certaine durée ou lorsque le personnage
touche l'adversaire.

</td>
</tr>
<tr>
<td style="padding:20px" colspan="2">
<center>

***Charm***  
  
![](/images/Charm_p4.jpg "/images/Charm_p4.jpg")

</center>

  
Le personnage perd continument des SP au cours du temps qui sont gagnés
par l'adversaire. Expire après une certaine durée ou lorsque le
personnage touche l'adversaire.

</td>
</tr>
</table>

# Burst

La jauge de burst se recharge automatiquement à une vitesse d'environ
1,11% par seconde (exactement 90 secondes pour se remplir à 100%). Il
existe des moyens de remplir la jauge plus rapidement :

- Toucher avec l'autocombo
- Subir des dégâts

D'autre part les différents burst ont des propriétés différentes en
fonction du type de burst utilisé. Un Burst dure 68 frames (dont 16 de
startup) et est invulnérable sur les frames 1 à 28. Il est néanmoins
terriblement unsafe en garde comme on pourrait l'imaginer, laissant à un
frame advantage de -19. En revanche les Max Burst et One More Burst sont
plus rapides avec une durée de 35 frame (dont 14 de startup) mais une
invulnérabilité sur les frames 1 à 21. Ces deux burst donnent cependant
un frame advantage de +10.
