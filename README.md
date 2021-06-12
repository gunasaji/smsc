# smsc

SMS Classifier App

Cara menjalankan:

1. Buat composer network:

    cd ~/fabric-dev-servers
    export FABRIC_VERSION=hlfv11
    ./startFabric.sh
    ./createPeerAdminCard.sh
    
    cd ~/downloads/smsc
    
    composer network install --card PeerAdmin@hlfv1 --archiveFile smsc@0.0.1.bna
    
    composer network start --networkName smsc --networkVersion 0.0.1 --networkAdmin admin --networkAdminEnrollSecret adminpw --card PeerAdmin@hlfv1 --file networkadmin.card
    
    composer card import --file networkadmin.card
    
    composer network ping --card admin@tutorial-network

2. REST API:

    composer-rest-server
admin@smsc
never use name spaces
no
no
yes
enter
yes
no
--> cek di localhost:3000

3. WebApp: 
cd SMSC-App
npm start
--> cek di localhost:4200
