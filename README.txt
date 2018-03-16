L'application chat/serveur contient 3 programmes
	- le serveur
	- l'application client
	- le chat en lui même

Afin d'utiliser correctement le programme,
veuillez suivre les étapes suivantes :

- remplacer "localhost" dans le programme clientServer
par l'adresse du pc où se trouvera le serveur

- lancer chatServeur_V2

- lancer clientServer

- clientServer répond aux commandes suivantes :

	connection <pseudo> : a pour effet de connecter le client,
	enregistrer son pseudo et rendre le chat accessible

	clients : revoie la liste des clients connectés

	chat : lance le chat dans la fenêtre où se trouve l'utilisateur
	(même fenêtre que l'application clientServer)

	deconnection : supprime l'utilisateur de la liste des utilisateurs
	connectés

- se connecter via la commande "connection <pseudo>"

- lancer le chat via la commande chat

- le chat répond aux commandes suivantes :

	/join <adresse> <port> : enregistre l'adresse du destinataire

	/send <message> : envoie un message à l'utilisateur qui a été joint

	/client : renvoie les données de l'utilisateur avec lequel on communique

	/quit : arrête la connection au client

	/exit : arrête le chat

- quitter le chat

- se déconnecter

- fermer la fenêtre clientServer

Notes :

	- L'application est en 3 parties, la prochaine version comportera uniquement deux
	programmes.

	- L'application ne permet pas à l'utilisateur d'une machine de démarrer deux chats
	en même temps. La prochaine version le permettra.

	- Les programmes ne sont pas très robustes et peuvent planter facilement.

	 -Le serveur ne peut pas être lancé depuis le shell, car le shell n'accepte pas les
	connections de clients venant d'autres pcs.

	- Un client qui quitte la fenêtre clientServer sans se déconnecter laisse ses
	informations dans la liste de clients connectés. La prochaine version prendra en
	charge le problème.

	- La gestion des pseudos n'est pas tout à fait au point

	- La prochaine version utilisera des objets clients pour sotcker les données
	de ces derniers

Description des protocoles :

connection "clientServer - chatServer" : protocole TCP. Le serveur est capable d'écouter les 
requêtes de plusieurs clients grâce au module select. Le serveur enregistre les coordonnées
des clients qui tentent de se connecter dans une liste et parcourt cette liste pour écouter à
tour de rôle les requêtes des clients.

connection "chat-chat" : protocole UDP. Le client envoie et reçoit des données sans avoir
besoin de se connecter.
