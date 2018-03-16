L'application chat/serveur contient 3 programmes
	- le serveur
	- l'application client
	- le chat en lui m�me

Afin d'utiliser correctement le programme,
veuillez suivre les �tapes suivantes :

- remplacer "localhost" dans le programme clientServer
par l'adresse du pc o� se trouvera le serveur

- lancer chatServeur_V2

- lancer clientServer

- clientServer r�pond aux commandes suivantes :

	connection <pseudo> : a pour effet de connecter le client,
	enregistrer son pseudo et rendre le chat accessible

	clients : revoie la liste des clients connect�s

	chat : lance le chat dans la fen�tre o� se trouve l'utilisateur
	(m�me fen�tre que l'application clientServer)

	deconnection : supprime l'utilisateur de la liste des utilisateurs
	connect�s

- se connecter via la commande "connection <pseudo>"

- lancer le chat via la commande chat

- le chat r�pond aux commandes suivantes :

	/join <adresse> <port> : enregistre l'adresse du destinataire

	/send <message> : envoie un message � l'utilisateur qui a �t� joint

	/client : renvoie les donn�es de l'utilisateur avec lequel on communique

	/quit : arr�te la connection au client

	/exit : arr�te le chat

- quitter le chat

- se d�connecter

- fermer la fen�tre clientServer

Notes :

	- L'application est en 3 parties, la prochaine version comportera uniquement deux
	programmes.

	- L'application ne permet pas � l'utilisateur d'une machine de d�marrer deux chats
	en m�me temps. La prochaine version le permettra.

	- Les programmes ne sont pas tr�s robustes et peuvent planter facilement.

	 -Le serveur ne peut pas �tre lanc� depuis le shell, car le shell n'accepte pas les
	connections de clients venant d'autres pcs.

	- Un client qui quitte la fen�tre clientServer sans se d�connecter laisse ses
	informations dans la liste de clients connect�s. La prochaine version prendra en
	charge le probl�me.

	- La gestion des pseudos n'est pas tout � fait au point

	- La prochaine version utilisera des objets clients pour sotcker les donn�es
	de ces derniers

Description des protocoles :

connection "clientServer - chatServer" : protocole TCP. Le serveur est capable d'�couter les 
requ�tes de plusieurs clients gr�ce au module select. Le serveur enregistre les coordonn�es
des clients qui tentent de se connecter dans une liste et parcourt cette liste pour �couter �
tour de r�le les requ�tes des clients.

connection "chat-chat" : protocole UDP. Le client envoie et re�oit des donn�es sans avoir
besoin de se connecter.
