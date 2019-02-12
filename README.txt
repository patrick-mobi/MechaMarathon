# MechaMarathon
A multiplayer game about piloting a robot across a trap-filled playing field to checkpoints before the others do the same







##########################################
##########################################
##########################################
USER INTERFACE

zwei optionen: spiel hosten, spiel beitreten
hosten: qr-code wird angezeigt
beitreten: qr-scanner wird geöffnet




game screen
  upper half
    two tabs, player chooses
      board watching
      player loadout watching
  lower half
    either own cards + programming registers
    or upgrade shop (based on play phase)
    
    
##########################################
##########################################
##########################################
RUNDENABLAUF

startplatz festlegen (in login-reihenfolge)

1.phase
upgrade shop: (spielerzahl - offene upgrades) vom zugstapel aufdecken

reihenfolge festlegen

in reihenfolge spielerprompt: upgrade kaufen?

wenn niemand kauft, offene upgrades ablegen


2. phase
countdown zum programmieren
alle spieler: x karten vom zugstapel auf die hand

spieler programmieren ihre Register, erster drückt sanduhr
countdown für alle: 30 sekunden

ende der klickphase

3. phase
1-5 register

reihenfolge festlegen

in reihenfolge bewegungen ausführen

board elemente ausführen






##########################################
##########################################
##########################################
PROGRAMMING STUFF




board tiles:
neutral
start
radar
wall
pit

perm hazard: wall, pit, cliff, portal,
temp hazard: laser, conveyor, gear,

object: board
tile type layout
energy cubes
victory tokens

objekt:upgrade shop
zugstapel upgrades
ablagestapel upgrades
offene upgrades

new upgrade ideas:
lay down energy cubes
rotate game tile









