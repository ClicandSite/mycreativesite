"""15/11/2026 (audit SEO) : texte propre à chaque page métier « modèle », pour qu'elles ne se ressemblent plus.
Chaque entrée : liste de (titre H2, [paragraphes]). Fusionné dans la page par build_seo.page() si la page n'a pas déjà un « body »."""

BODY = {}

BODY["site-internet-dentiste"] = [
  ("Informer les patients sans faire de publicité", [
    "Depuis la réforme de 2020, un chirurgien-dentiste peut présenter son cabinet en ligne, à condition que l'information reste loyale, claire et utile au patient. Le modèle est écrit dans cet esprit : vos actes, vos équipements, vos horaires, l'accès au cabinet, sans superlatif ni promesse de résultat.",
    "Seuls les titres reconnus apparaissent (orthopédie dento-faciale, chirurgie orale, médecine bucco-dentaire). Une orientation d'exercice comme l'implantologie ou la pédodontie se présente comme une activité du cabinet, pas comme une spécialité."]),
  ("Les questions que se posent vos patients", [
    "Avant d'appeler, un patient veut savoir si vous prenez de nouveaux patients, si le cabinet est accessible en fauteuil roulant, quels moyens de paiement vous acceptez et s'il existe un parking. Le site y répond en une page, ce qui évite une partie des appels au secrétariat.",
    "Pour les urgences, une rubrique dédiée explique comment vous joindre aux heures d'ouverture et renvoie vers le service de garde du département le week-end et les jours fériés."]),
  ("Honoraires et devis", [
    "L'information sur les honoraires est une obligation : le site rappelle votre conventionnement et indique que les soins prothétiques font l'objet d'un devis remis avant le traitement, avec ce qui relève du 100 % Santé. Vous gardez la main sur ces textes depuis votre espace client."]),
]

BODY["site-internet-kinesitherapeute"] = [
  ("Présenter vos domaines de rééducation", [
    "Un patient qui sort d'une opération du genou ne cherche pas la même chose qu'une jeune mère pour une rééducation périnéale ou un sportif qui revient de blessure. Le site présente chaque domaine que vous pratiquez sur sa propre rubrique : orthopédie, rééducation post-opératoire, sport, respiratoire, vestibulaire, périnéale.",
    "Les textes restent informatifs, comme le veut le code de déontologie : ils expliquent comment se déroulent les séances, combien de temps elles durent et ce qu'il faut apporter (ordonnance, examens, tenue)."]),
  ("Cabinet et domicile", [
    "Si vous vous déplacez chez les patients, le site indique clairement les communes desservies et les cas où le déplacement est possible. Le patient sait tout de suite s'il peut vous appeler, ce qui limite les demandes hors secteur.",
    "Pour le cabinet : plateau technique, accessibilité, parking, transports en commun. Ce sont souvent ces détails qui décident un patient entre deux cabinets proches."]),
  ("Remboursement et prise de rendez-vous", [
    "Une rubrique rappelle votre conventionnement, la prise en charge sur prescription et les dépassements éventuels. La demande de rendez-vous en ligne permet au patient d'indiquer son motif et ses disponibilités : vous le rappelez avec un créneau adapté, sans logiciel de réservation payé à la commission."]),
]

BODY["site-internet-veterinaire"] = [
  ("Ce que cherchent les propriétaires d'animaux", [
    "Horaires, urgences, espèces soignées : ce sont les trois premières questions. Le site les affiche dès l'accueil, avec un bouton d'appel toujours visible sur téléphone. Si vous soignez les NAC, les équidés ou les animaux de rente, une rubrique le précise, car beaucoup de cliniques ne le font pas.",
    "La présentation de l'équipe compte aussi : vétérinaires, auxiliaires spécialisées, domaines d'intérêt (dentisterie, imagerie, comportement), dans le respect du code de déontologie vétérinaire."]),
  ("Urgences et continuité des soins", [
    "Une page explique ce qu'il faut faire en dehors des heures d'ouverture : votre numéro de garde ou le service d'urgences vers lequel vous orientez. Elle donne aussi les bons réflexes en attendant (intoxication, coup de chaleur, plaie), ce qui rassure et vous fait gagner du temps au téléphone."]),
  ("Prévention et tarifs", [
    "Vaccins, identification, stérilisation, vermifuges, alimentation : des rubriques de prévention qui répondent aux questions courantes et amènent des visites sur Google. L'affichage des tarifs des actes courants, obligatoire en clinique, peut être repris sur le site et mis à jour depuis votre espace client."]),
]

BODY["site-internet-chambres-d-hotes-gite"] = [
  ("Réserver en direct plutôt que payer une commission", [
    "Les grandes plateformes de réservation prennent souvent 15 à 20 % du prix de chaque nuit. Votre site ne remplace pas ces plateformes du jour au lendemain, mais il capte les clients qui vous ont trouvés une première fois et reviennent, ceux qui cherchent votre nom sur Google, et ceux à qui un ami vous a recommandé.",
    "Le visiteur choisit ses dates et sa chambre, la demande arrive dans votre boîte mail et votre espace « Mes clients », et vous confirmez vous-même. Pas de commission, pas d'intermédiaire."]),
  ("Chambres d'hôtes ou meublé de tourisme : ce que le site doit dire", [
    "Une chambre d'hôtes, c'est au plus cinq chambres et quinze personnes, chez l'habitant, petit-déjeuner compris, avec une déclaration en mairie. Un gîte est en général un meublé de tourisme, déclaré lui aussi, parfois classé en étoiles. Le site affiche ces informations, le classement s'il existe et la taxe de séjour, ce qui rassure les voyageurs.",
    "Chaque chambre ou logement a sa fiche : couchages, salle d'eau, vue, accessibilité, animaux acceptés ou non."]),
  ("Donner envie de venir", [
    "Les photos font la réservation : le modèle met en avant une grande galerie, la table d'hôtes si vous en proposez une, et les alentours (randonnées, plages, villages, restaurants que vous conseillez). Une version anglaise est disponible pour la clientèle étrangère."]),
]

BODY["site-internet-tourisme-loisirs"] = [
  ("Remplir vos créneaux, saison après saison", [
    "Kayak, randonnée guidée, visite de ville, parapente, escape game, plongée : votre activité se vend par créneaux. Le site présente chaque sortie avec sa durée, son niveau, l'âge minimum, le point de rendez-vous et le prix, puis reçoit les demandes de réservation pour une date précise.",
    "En haute saison, les questions sont toujours les mêmes ; une FAQ claire (que faut-il apporter, que se passe-t-il s'il pleut, peut-on venir en groupe) vous évite de répondre dix fois par jour au téléphone."]),
  ("Rassurer avant la réservation", [
    "Encadrement diplômé, assurance, matériel fourni, conditions d'annulation et météo : un visiteur qui découvre votre activité veut savoir qu'il est entre de bonnes mains. Le site le dit simplement, avec vos diplômes et agréments s'ils sont exigés pour votre activité.",
    "Les groupes, les comités d'entreprise et les écoles ont leur propre rubrique avec une demande de devis dédiée."]),
  ("Être trouvé par les touristes", [
    "Les vacanciers cherchent « activité » ou « que faire » suivi du nom du lieu, souvent depuis leur téléphone et souvent en anglais. Le site est rapide sur mobile, indique précisément le lieu de l'activité et existe en version anglaise."]),
]

BODY["site-internet-evenementiel"] = [
  ("Vendre une date, pas un produit", [
    "DJ, wedding planner, décorateur, location de matériel, animateur, photobooth : dans l'événementiel, le client a d'abord une date et un lieu. Le formulaire du site commence donc par là : type d'événement, date, lieu, nombre d'invités. Vous savez tout de suite si vous êtes disponible et si la demande vous intéresse.",
    "Les demandes arrivent par mail et dans votre espace « Mes clients », où vous suivez chaque devis jusqu'à la signature."]),
  ("Montrer vos événements passés", [
    "Rien ne convainc mieux qu'une galerie d'événements réels : mariage champêtre, soirée d'entreprise, anniversaire, gala. Le modèle classe vos réalisations par type d'événement pour que chaque client se projette dans le sien.",
    "Vos formules et vos options (heures supplémentaires, éclairage, déplacement) sont présentées clairement, avec un prix de départ si vous le souhaitez."]),
  ("Les mariages se préparent tôt", [
    "Un couple réserve souvent ses prestataires un an à l'avance, à partir de recherches sur Google comme « DJ mariage » suivi de la région. Le site indique votre zone d'intervention et les lieux de réception où vous avez déjà travaillé, ce qui aide à être trouvé sur ces recherches."]),
]

BODY["site-internet-location-demenagement"] = [
  ("Un devis juste, du premier coup", [
    "Pour un déménagement, le prix dépend du volume, des étages, de l'ascenseur, de la distance et des dates. Le formulaire du site demande ces informations dès le départ : vous faites un devis juste sans rappeler trois fois le client. Pour la location de véhicules, le client choisit la catégorie, les dates et le kilométrage souhaité.",
    "Chaque demande arrive dans votre espace « Mes clients », d'où vous envoyez un devis en PDF à votre nom."]),
  ("Ce que le client doit savoir avant de réserver", [
    "Location : âge minimum, années de permis, caution, franchise, carburant, horaires de retrait et de retour. Déménagement : ce qui est compris (cartons, démontage, emballage), l'assurance des biens transportés et votre inscription au registre des transporteurs. Ces informations, affichées clairement, évitent les litiges.",
    "Vous les mettez à jour vous-même, par exemple quand vous changez vos tarifs de haute saison."]),
  ("Les périodes de pointe", [
    "Fin de mois, été, rentrée : les demandes se concentrent. Un site qui reçoit les demandes à toute heure vous permet de remplir votre planning à l'avance, sans dépendre uniquement des comparateurs."]),
]

BODY["site-internet-services-a-domicile"] = [
  ("Le crédit d'impôt, premier argument de vente", [
    "Ménage, repassage, jardinage, petit bricolage, garde d'enfants, aide aux seniors : si votre entreprise est déclarée comme organisme de services à la personne, vos clients bénéficient d'un crédit d'impôt de 50 % des sommes payées, dans les limites prévues par la loi. Le site l'explique simplement, exemple chiffré à l'appui.",
    "Si vous proposez l'avance immédiate de crédit d'impôt avec l'Urssaf, le client ne paie que la moitié tout de suite : c'est un argument fort, mis en avant dès l'accueil."]),
  ("Votre zone et vos services, clairement", [
    "Le client veut savoir si vous intervenez dans sa commune et à quelle fréquence. Le site liste vos communes, vos services et vos formules (ponctuel, hebdomadaire, saisonnier). Pour l'aide aux personnes âgées ou handicapées, il indique votre agrément ou autorisation lorsque l'activité l'exige.",
    "La demande de devis précise le service, la surface ou le nombre d'heures, et la fréquence souhaitée."]),
  ("La confiance avant tout", [
    "On fait entrer un intervenant chez soi : présentez votre équipe, votre façon de recruter, votre assurance et la continuité en cas d'absence. Ce sont ces informations qui décident un client à vous appeler plutôt qu'un concurrent."]),
]

BODY["site-internet-coiffeur-institut-beaute"] = [
  ("Des prestations et des prix lisibles", [
    "Coupe femme, homme, enfant, couleur, balayage, lissage, soins du visage, épilation, onglerie : chaque prestation a sa durée et son prix. L'affichage des prix est obligatoire en salon ; le site le reprend, ce qui évite la mauvaise surprise et rassure les nouvelles clientes.",
    "Vous modifiez vos tarifs et vos prestations vous-même depuis votre espace client, par exemple quand vous lancez une nouvelle technique."]),
  ("Prendre rendez-vous sans décrocher", [
    "Quand vous avez les mains dans une couleur, vous ne pouvez pas répondre au téléphone. La demande de rendez-vous en ligne permet à la cliente de choisir sa prestation et son créneau souhaité ; vous confirmez entre deux clientes.",
    "Le site renvoie aussi vers votre Instagram, où vous publiez vos réalisations, et propose des cartes cadeaux, très demandées à Noël et pour la fête des mères."]),
  ("Être trouvé dans votre quartier", [
    "Les recherches « coiffeur » ou « institut de beauté » se font presque toujours avec un nom de quartier ou de ville, depuis un téléphone. Le site met en avant votre adresse, vos horaires et un plan, et se relie à votre fiche Google."]),
]

BODY["site-internet-masseur-osteopathe-bien-etre"] = [
  ("Les bons mots pour votre pratique", [
    "Les mots comptent : le massage à visée thérapeutique est réservé aux masseurs-kinésithérapeutes, et les praticiens bien-être parlent plutôt de modelage, de soin ou de relaxation. L'ostéopathe, lui, exerce sous un titre protégé et ne promet pas de guérison. Le modèle est rédigé avec ces précautions, pour que votre site reste dans les clous.",
    "Chaque pratique (ostéopathie, sophrologie, réflexologie, modelage, shiatsu, naturopathie) a sa propre présentation : ce qu'elle est, comment se passe une séance, ce qu'elle n'est pas."]),
  ("Lever les hésitations", [
    "Beaucoup de personnes n'osent pas prendre un premier rendez-vous parce qu'elles ne savent pas à quoi s'attendre. Le site explique le déroulé, la durée, la tenue conseillée, les contre-indications éventuelles, et si certaines mutuelles remboursent une partie des séances.",
    "Les cartes cadeaux sont aussi proposées : c'est une part importante du chiffre d'affaires des praticiens bien-être."]),
  ("Cabinet, domicile ou entreprise", [
    "Si vous intervenez à domicile ou en entreprise, une rubrique le présente avec votre zone. Les demandes de rendez-vous arrivent directement chez vous, sans plateforme à la commission."]),
]

BODY["site-internet-toiletteur"] = [
  ("Des tarifs selon la race et le gabarit", [
    "Un bain pour un yorkshire et une tonte pour un bouvier bernois n'ont rien à voir. Le site présente vos tarifs par gabarit ou par race, avec les suppléments éventuels (démêlage, chien difficile), et le formulaire de rendez-vous demande la race, l'âge et l'état du pelage.",
    "Vous arrivez au rendez-vous en sachant déjà combien de temps prévoir."]),
  ("Montrer vos résultats", [
    "Les photos avant-après sont votre meilleure publicité : le modèle leur réserve une galerie, que vous alimentez depuis votre téléphone. Vous pouvez aussi présenter votre façon de travailler : sans cage, sans tranquillisant, avec des produits adaptés, accueil des chats et des NAC.",
    "Si vous proposez un toilettage à domicile ou en camion, le site indique votre zone de passage."]),
  ("Fidéliser vos clients", [
    "Un chien se toilette toutes les six à huit semaines : rappelez sur le site la fréquence conseillée par type de pelage et proposez de fixer le prochain rendez-vous. Les bons cadeaux et les produits que vous vendez en boutique peuvent aussi y figurer."]),
]

BODY["site-internet-traiteur"] = [
  ("Un devis par nombre de convives", [
    "Mariage, baptême, séminaire, buffet d'entreprise, plateaux-repas : le formulaire demande la date, le lieu, le nombre de convives et le type de service (livré, servi, buffet, cocktail). Vous répondez avec un devis précis, envoyé en PDF à votre nom depuis votre espace client.",
    "Vos menus et vos formules sont présentés avec un prix par personne de départ, ce qui filtre les demandes hors budget."]),
  ("Allergènes et informations obligatoires", [
    "La réglementation impose d'informer le client sur les 14 allergènes majeurs. Le site indique comment vous le faites (carte détaillée, information sur demande) et propose des options pour les régimes particuliers : végétarien, sans gluten, halal, casher si vous les proposez.",
    "Votre zone de livraison, les délais de commande et les conditions d'annulation sont clairement indiqués."]),
  ("Les entreprises, une clientèle régulière", [
    "Petits-déjeuners, déjeuners de travail, cocktails de fin d'année : les entreprises commandent souvent et paient bien. Une rubrique leur est dédiée, avec facture et devis rapides."]),
]

BODY["site-internet-photographe"] = [
  ("Votre portfolio d'abord", [
    "Un client choisit un photographe sur ses images. Le modèle laisse toute la place à vos photos, en grand, classées par type de prestation : mariage, portrait, famille, naissance, entreprise, immobilier, produit. Chaque galerie se charge vite, même sur téléphone, sans perdre en qualité.",
    "Vous ajoutez et retirez vos images vous-même depuis votre espace client."]),
  ("Des formules claires", [
    "Durée de présence, nombre de photos livrées, délai de livraison, retouches, album, droits d'utilisation pour les entreprises : présenter vos formules évite les malentendus. Le formulaire de contact demande le type de séance, la date et le lieu.",
    "Pour les mariages, une rubrique dédiée répond aux questions habituelles : déplacements, second photographe, acompte."]),
  ("Être trouvé localement", [
    "Les clients cherchent « photographe mariage » ou « photographe portrait » suivi d'une ville. Le site précise votre zone, vos lieux de séance préférés et se relie à votre fiche Google et à votre Instagram."]),
]

BODY["site-internet-fleuriste"] = [
  ("Commander sans passer par un réseau", [
    "Les réseaux de transmission florale prennent une part importante de chaque commande. Avec votre site, le client commande directement chez vous : bouquet, composition, plante, livraison dans votre zone ou retrait en boutique.",
    "Vous gérez vos créations, vos prix et vos créneaux de livraison depuis votre espace client."]),
  ("Deuil, mariage, entreprise", [
    "Ces trois clientèles ont chacune leur rubrique. Le deuil demande du tact et de la rapidité : gerbes, couronnes, coussins, livraison au funérarium ou à l'église. Le mariage se prépare des mois à l'avance avec un rendez-vous. Les entreprises recherchent un abonnement floral pour leur accueil.",
    "Chaque rubrique a son formulaire adapté."]),
  ("Les temps forts de l'année", [
    "Saint-Valentin, fête des grands-mères, fête des mères, Toussaint, Noël : le site met en avant vos créations de saison et vos horaires exceptionnels. Ce sont les jours où les clients cherchent un fleuriste sur Google, souvent à la dernière minute."]),
]

BODY["site-internet-location-bateau"] = [
  ("Avec ou sans permis, avec ou sans skipper", [
    "La première question d'un client : peut-il louer sans permis ? Le site sépare clairement les bateaux sans permis, les bateaux avec permis et les sorties avec skipper, avec pour chacun le nombre de passagers, la puissance, la durée de location et le prix.",
    "La demande de réservation indique la date, la durée et le nombre de personnes ; vous confirmez selon la météo et vos disponibilités."]),
  ("Les conditions, noir sur blanc", [
    "Caution, carburant, zone de navigation autorisée, équipements de sécurité, annulation en cas de mauvais temps : ces règles, affichées avant la réservation, évitent les discussions sur le ponton.",
    "Une version anglaise est disponible : une grande partie de la clientèle de location est étrangère."]),
  ("Votre port, vos balades", [
    "Présentez votre port de départ, le parking, et les balades possibles : calanques, îles, criques, couchers de soleil. Ce sont ces idées de sorties qui font rêver et décident à réserver."]),
]

BODY["site-internet-bijouterie"] = [
  ("Plus qu'une vitrine", [
    "Une bijouterie-horlogerie vit aussi de ses services : réparation, mise à taille, gravure, pile et révision de montre, création sur mesure, transformation d'anciens bijoux. Le site présente chacun d'eux avec un délai indicatif et invite à passer en boutique ou à demander un devis.",
    "Ces services amènent des visites régulières, et ce sont des recherches fréquentes sur Google."]),
  ("Rachat d'or et confiance", [
    "Si vous rachetez de l'or, le site explique le déroulé : estimation en boutique, pièce d'identité obligatoire, paiement par virement ou chèque conformément à la réglementation. Cette transparence vous distingue des comptoirs anonymes.",
    "Vos marques distribuées, vos certificats et vos garanties sont affichés pour rassurer."]),
  ("Les grandes occasions", [
    "Fiançailles, mariage, naissance, anniversaire : une rubrique par occasion, avec vos conseils et une prise de rendez-vous pour un moment au calme en boutique."]),
]

BODY["site-internet-profession-liberale"] = [
  ("Avocat, expert-comptable, architecte, consultant…", [
    "Chaque profession réglementée a ses règles de communication, fixées par son ordre ou sa chambre : informations autorisées, mentions obligatoires, ton à adopter. Le modèle reste sobre et factuel, et vous indiquez vos mentions propres : barreau, numéro d'inscription à l'ordre, assurance de responsabilité civile professionnelle.",
    "Vos domaines d'intervention sont présentés un par un, avec le type de client que vous accompagnez."]),
  ("Expliquer votre façon de travailler", [
    "Premier rendez-vous, mode de facturation (forfait, temps passé, honoraires de résultat lorsque c'est permis), délais, rendez-vous en visio : un client hésite moins quand il sait comment se passe la collaboration. Le formulaire de contact recueille l'objet de la demande pour que vous prépariez le premier échange.",
    "Vous pouvez publier des articles sur les questions que vos clients vous posent souvent : c'est aussi ce qui vous fait trouver sur Google."]),
]

BODY["site-internet-infirmier-liberal"] = [
  ("Être joint facilement par les patients", [
    "Un patient qui sort de l'hôpital ou un proche qui organise des soins cherche un infirmier disponible dans sa commune, souvent en urgence. Le site affiche votre numéro en grand, vos communes de tournée et vos horaires de permanence au cabinet si vous en tenez une.",
    "La demande de prise en charge indique le type de soin, l'adresse et la date de début : vous rappelez avec une réponse claire."]),
  ("Les soins que vous réalisez", [
    "Prises de sang, injections, pansements, perfusions, soins post-opératoires, diabète, soins d'hygiène, chimiothérapie à domicile : chaque soin est présenté de façon informative, dans le respect des règles de communication de la profession.",
    "Le site rappelle que les soins sur prescription sont pris en charge par l'Assurance maladie et indique le tiers payant si vous le pratiquez."]),
  ("Un cabinet à plusieurs", [
    "Si vous exercez en cabinet de groupe, le site présente chaque infirmier et explique l'organisation des remplacements, pour que le patient sache qu'il sera suivi tous les jours de la semaine."]),
]

BODY["site-internet-boulangerie"] = [
  ("Les commandes qui font le chiffre", [
    "Galettes des rois, bûches, pièces montées, gâteaux d'anniversaire, plateaux de viennoiseries pour les entreprises : ces commandes se préparent à l'avance. Le site permet de les passer en ligne avec la date de retrait, et vous les retrouvez dans votre espace client.",
    "Fini les commandes notées sur un papier qui se perd."]),
  ("Horaires, jours de fermeture, spécialités", [
    "La question la plus fréquente sur Google : « boulangerie ouverte » le dimanche ou le lundi. Le site affiche vos horaires, vos jours de fermeture et vos congés, et vous les modifiez en un instant.",
    "Vos pains spéciaux, votre levain, vos farines locales, vos labels : c'est ce qui vous distingue de la chaîne voisine. Seul celui qui pétrit et cuit sur place peut se dire boulanger, autant le dire."]),
  ("Les allergènes", [
    "L'information sur les allergènes est obligatoire : le site indique comment vous la donnez et peut présenter vos produits sans gluten ou vegan si vous en faites."]),
]

BODY["site-internet-artisan-batiment"] = [
  ("Ce que vérifie un client avant de vous appeler", [
    "Avant de confier un chantier, un particulier vérifie votre sérieux : numéro SIRET, assurance décennale, ancienneté, réalisations, avis. Le site affiche ces informations dès l'accueil. La mention de l'assurance décennale est obligatoire sur vos devis et vos factures ; la montrer sur le site rassure dès le premier contact.",
    "Si vous êtes RGE, le site le met en avant : c'est la condition pour que vos clients touchent certaines aides à la rénovation énergétique."]),
  ("Vos chantiers en photos", [
    "Salle de bains, cuisine, extension, toiture, façade, isolation : une galerie avant-après par type de chantier vaut tous les discours. Vous l'alimentez depuis votre téléphone, à la fin de chaque chantier.",
    "Le formulaire de devis demande le type de travaux, la surface, la commune et des photos : vous pouvez estimer avant de vous déplacer."]),
  ("Votre zone d'intervention", [
    "Le site liste les communes où vous travaillez, pour apparaître sur les recherches comme « maçon » ou « carreleur » suivies du nom de la ville."]),
]

BODY["site-internet-restaurant"] = [
  ("Réservation sans commission par couvert", [
    "Les plateformes de réservation facturent souvent chaque couvert ou un abonnement élevé. Avec votre site, le client réserve directement chez vous : date, heure, nombre de personnes. Vous confirmez, et vous gardez le contact de vos clients.",
    "Les plateformes peuvent rester un complément ; votre site devient la porte d'entrée principale."]),
  ("La carte à jour, tout le temps", [
    "Le client veut voir la carte et les prix avant de venir. Vous la modifiez vous-même depuis votre espace client, plat du jour et ardoise compris, sans PDF à refaire. Les allergènes, obligatoires, sont indiqués.",
    "Privatisation, groupes, événements, vente à emporter : chaque service a sa rubrique."]),
  ("Être trouvé à l'heure du repas", [
    "Les recherches « restaurant » suivi d'un quartier explosent à 12 h et à 19 h, presque toutes sur téléphone. Le site s'affiche vite, met en avant vos horaires, votre adresse et un bouton d'appel, et se relie à votre fiche Google."]),
]

BODY["site-internet-vtc"] = [
  ("Sortir de la dépendance aux applications", [
    "Les applications de VTC prélèvent une part importante de chaque course. Un site à votre nom vous apporte une clientèle directe : hôtels, entreprises, clients réguliers, touristes qui réservent leur transfert à l'avance. Chaque course réservée sur votre site est payée entièrement à vous.",
    "La réservation préalable étant obligatoire pour un VTC, le formulaire de réservation est au centre du site : départ, arrivée, date, heure, passagers, bagages."]),
  ("Forfaits et transferts", [
    "Aéroport, gare, mise à disposition à l'heure, événements : afficher des forfaits clairs rassure et accélère la décision. Vous les modifiez vous-même depuis votre espace client.",
    "Le site présente votre véhicule, vos équipements (sièges enfant, eau, wifi) et les langues que vous parlez ; une version anglaise est disponible pour la clientèle étrangère."]),
  ("Vos mentions professionnelles", [
    "Carte professionnelle VTC, inscription au registre, assurance : affichées sur le site, elles prouvent votre sérieux face aux offres non déclarées."]),
]

BODY["site-internet-coach-sportif"] = [
  ("Votre méthode, vos résultats", [
    "Perte de poids, prise de masse, préparation physique, remise en forme après une grossesse, sport santé pour les seniors : présentez chaque objectif et la façon dont vous y répondez. Le client se reconnaît dans une situation précise, pas dans une promesse générale.",
    "Les témoignages de vos clients et leurs progrès (avec leur accord) complètent la présentation."]),
  ("Où et comment vous coachez", [
    "À domicile, en extérieur, en salle, en visio, en petit groupe ou en entreprise : le site précise vos lieux, votre zone de déplacement, et vos formules (séance unique, carnet de séances, abonnement). Un bilan ou une première séance découverte peut être réservé en ligne.",
    "Votre carte professionnelle d'éducateur sportif et vos diplômes sont affichés : ils sont exigés pour encadrer contre rémunération, et vos clients le savent de plus en plus."]),
]

BODY["site-internet-auto-ecole"] = [
  ("Les formations, une par une", [
    "Permis B en boîte manuelle ou automatique, conduite accompagnée, conduite supervisée, permis moto, code, stages accélérés, passerelle boîte auto : chaque formation a sa page avec son déroulé, sa durée et son prix. Le futur élève compare sans avoir à appeler.",
    "Si vos formations sont éligibles au CPF ou au permis à 1 € par jour, le site l'indique clairement : c'est souvent ce qui décide les jeunes et leurs parents."]),
  ("Ce qui vous distingue des plateformes", [
    "Moniteurs présents en agence, voitures récentes, suivi personnalisé, horaires de bureau, accompagnement à l'examen : le site met en avant ce que les auto-écoles en ligne n'offrent pas. Votre numéro d'agrément préfectoral et vos taux de réussite sont affichés.",
    "La demande d'inscription ou de rendez-vous arrive directement chez vous."]),
]

BODY["site-internet-agence-immobiliere"] = [
  ("Vos annonces et vos obligations", [
    "Une agence doit afficher ses honoraires, sa carte professionnelle, son garant financier, et chaque annonce doit donner le classement énergétique (DPE) et les informations sur la copropriété. Le modèle prévoit ces mentions, pour que votre site soit en règle dès le premier jour.",
    "Chaque bien a sa propre page, que Google peut indexer, avec photos, prix, surface et contact direct."]),
  ("Attirer des vendeurs, pas seulement des acheteurs", [
    "Les mandats font l'agence. Une page d'estimation gratuite et une présentation de votre méthode de vente (photos, visites, suivi) incitent les propriétaires à vous contacter. Une rubrique sur votre secteur, vos quartiers et les prix constatés renforce votre image d'expert local.",
    "Avec le Pack Auto, Moto & Immo, vos biens sont aussi diffusés sur Abracadeal."]),
]

BODY["site-internet-concession-moto"] = [
  ("Neuf, occasion, atelier", [
    "Une concession moto vit de trois activités : la vente de neuf, l'occasion et l'atelier. Le site les présente toutes : votre stock d'occasions avec une page par moto, les marques que vous distribuez, et la prise de rendez-vous atelier pour l'entretien, les pneus ou la préparation du contrôle technique.",
    "Les équipements du pilote (casques, blousons, gants) peuvent aussi avoir leur rubrique."]),
  ("Les questions des motards", [
    "Reprise de l'ancienne moto, financement, permis A2 et bridage, garantie sur les occasions, essai : le site y répond et propose de prendre rendez-vous. Si vous proposez du financement, les mentions légales liées au crédit sont prévues.",
    "Chaque moto d'occasion est aussi diffusée sur Abracadeal avec le Pack Auto, Moto & Immo."]),
]

BODY["site-internet-concession-automobile"] = [
  ("Chaque véhicule a sa page", [
    "Un acheteur cherche un modèle précis, une motorisation, un budget. Avec une page par véhicule, indexable par Google, vos voitures apparaissent sur ces recherches. Photos, kilométrage, options, historique d'entretien et garantie : tout est sur la page, avec un bouton pour appeler ou réserver un essai.",
    "Vous ajoutez et retirez vos véhicules depuis votre espace client, en quelques minutes."]),
  ("Reprise, financement, garantie", [
    "Ce sont les trois questions qui font une vente. Le site propose une estimation de reprise, présente vos solutions de financement avec les mentions obligatoires du crédit, et détaille la garantie de chaque véhicule.",
    "Avec le Pack Auto, Moto & Immo, votre stock est aussi publié sur Abracadeal, sans ressaisie."]),
]

# 15/11/2026 (Anthony : « au top du top ») : les 5 métiers les plus disputés passent au niveau des pages enrichies (~1 100 mots)
BODY["site-internet-vtc"] += [
  ("Hôtels, conciergeries, entreprises : la clientèle qui revient", [
    "Un réceptionniste d'hôtel ou une conciergerie cherche un chauffeur fiable à qui confier ses clients, pas une application. Une page « Professionnels » présente vos conditions pour eux : réservation par mail ou téléphone, facturation mensuelle, bons de commande, chauffeur nommé. C'est souvent cette clientèle qui fait vivre un VTC toute l'année, en dehors des saisons touristiques.",
    "Depuis votre espace client, vous éditez devis et bons en PDF à votre nom, et vous retrouvez l'historique de chaque client professionnel."]),
  ("Être trouvé par les voyageurs", [
    "Les recherches qui rapportent sont précises : « VTC aéroport » suivi d'une ville, « chauffeur privé » et le nom d'une destination, « transfert gare ». Le site indique votre ville de base, les aéroports, gares, hôtels et lieux d'événements que vous desservez, avec un forfait pour chacun quand c'est possible. Il se charge vite sur téléphone, car la plupart des réservations se font depuis un mobile, parfois depuis le tapis à bagages.",
    "La version anglaise, incluse en Premium, compte beaucoup : sur les trajets aéroport, une grande partie des clients sont étrangers."]),
  ("Moins de commission, plus de marge", [
    "Faites le calcul sur un mois : chaque course passée par votre site au lieu d'une plateforme vous laisse la commission en entier. Quelques transferts par mois suffisent en général à payer l'abonnement du site, le reste est du bénéfice."]),
]
BODY["site-internet-restaurant"] += [
  ("Groupes, privatisations et événements", [
    "Anniversaire, repas d'entreprise, baptême, soirée de fin d'année : ces réservations rapportent plus qu'un service ordinaire, mais elles arrivent rarement par les plateformes. Une rubrique dédiée présente votre capacité, vos menus de groupe, la privatisation de la salle ou de la terrasse, et un formulaire demande la date, le nombre de convives et le budget par personne.",
    "Vous répondez avec un devis en PDF à votre nom, envoyé depuis votre espace client."]),
  ("Vente à emporter et livraison sans intermédiaire", [
    "Si vous faites de la vente à emporter, le site présente la carte à emporter, les horaires de retrait et un bouton pour appeler ou commander. Les applications de livraison peuvent rester un complément, mais les clients fidèles qui commandent chez vous directement vous laissent toute la marge.",
    "Les bons cadeaux sont aussi une bonne source de chiffre d'affaires, surtout en fin d'année."]),
  ("Ce que Google regarde pour un restaurant", [
    "Pour apparaître sur « restaurant » suivi d'un quartier, Google croise votre fiche Google, votre site et les avis. Le site renforce la fiche : même nom, même adresse, mêmes horaires, une carte lisible par Google, et des données structurées qui indiquent votre type de cuisine et votre fourchette de prix. Pensez à mettre le lien de votre site sur votre fiche Google : c'est souvent le premier clic des clients."]),
]
BODY["site-internet-artisan-batiment"] += [
  ("Des demandes de devis qui valent le déplacement", [
    "Le pire pour un artisan, c'est de se déplacer pour un devis qui n'aboutira jamais. Le formulaire du site trie en amont : type de travaux, surface ou quantité, commune, délai souhaité, budget approximatif et photos. Vous voyez tout de suite si le chantier vous intéresse et vous arrivez au rendez-vous avec une idée précise.",
    "Les demandes sont classées dans votre espace « Mes clients », avec leur statut (à rappeler, devis envoyé, accepté), et vous pouvez éditer un devis en PDF à votre nom."]),
  ("Les aides à la rénovation, un argument qui fait signer", [
    "MaPrimeRénov', certificats d'économies d'énergie, éco-prêt à taux zéro, TVA réduite : les particuliers savent que les aides existent mais ne savent pas lesquelles les concernent. Une page qui explique les grandes lignes et précise que vous êtes RGE (si c'est le cas) vous fait sortir du lot. Vous l'adaptez à vos travaux : isolation, pompe à chaleur, fenêtres, chauffage.",
    "Les règles des aides changent souvent : le texte reste général et renvoie vers France Rénov' pour le détail, et vous le mettez à jour vous-même."]),
  ("Votre métier, pas un artisan générique", [
    "Maçon, plaquiste, peintre, carreleur, couvreur, menuisier, chauffagiste : le site présente vos vrais savoir-faire, un par un, avec les photos de vos chantiers. Ce sont ces pages précises qui sortent sur Google quand un particulier tape le nom d'un métier suivi de sa ville."]),
]
BODY["site-internet-coiffeur-institut-beaute"] += [
  ("Des prestations qui se vendent mieux en ligne", [
    "Certaines prestations demandent qu'on rassure avant de réserver : un balayage, un lissage, des extensions de cils, une épilation définitive. Une fiche par prestation explique le déroulé, la durée, l'entretien après et le prix de départ, avec des photos de vos réalisations. La cliente arrive au salon décidée, et vous perdez moins de temps en explications.",
    "Les mariées ont leur rubrique : essai, coiffure et maquillage le jour J, déplacement sur le lieu de réception."]),
  ("Fidéliser sans logiciel coûteux", [
    "Une cliente fidèle revient toutes les six à huit semaines. Le site lui permet de redemander un rendez-vous en un clic, de voir vos nouveautés et vos offres du moment, et d'offrir une carte cadeau à une amie. Vos produits vendus en salon peuvent y être présentés pour qu'elle les demande à sa prochaine visite.",
    "Vous gardez la main sur tout depuis votre espace client : prestations, prix, horaires, congés, photos."]),
  ("Salon, institut ou à domicile", [
    "Si vous travaillez à domicile ou que vous louez un fauteuil, le site indique votre zone, vos jours de passage et vos frais de déplacement. C'est une vraie différence face aux grandes enseignes, qui ne se déplacent pas."]),
]
BODY["site-internet-agence-immobiliere"] += [
  ("Des pages qui travaillent votre secteur", [
    "Un vendeur qui cherche « estimation maison » suivi de sa commune doit tomber sur vous. Le site prévoit une page par quartier ou par commune que vous couvrez : ambiance, écoles, transports, types de biens et fourchettes de prix constatées. Ces pages vous positionnent comme l'agence qui connaît le secteur, et elles sortent sur Google pendant des années.",
    "Vous les rédigez avec votre connaissance du terrain ; le modèle fournit la structure."]),
  ("Location et gestion", [
    "Si vous faites de la location ou de la gestion locative, une rubrique s'adresse aux propriétaires bailleurs : vos services, vos honoraires, la garantie loyers impayés si vous la proposez. Pour les locataires, chaque annonce de location affiche le loyer, les charges, le dépôt de garantie et les honoraires à leur charge, comme l'exige la loi.",
    "Les demandes de visite et de dossier arrivent directement chez vous."]),
  ("Agent indépendant ou agence de quartier", [
    "Agent commercial rattaché à un réseau ou agence indépendante : le site met votre nom et votre visage en avant, ce que les portails ne font pas. Les vendeurs choisissent une personne de confiance, pas une liste d'annonces."]),
]

FAQ_EXTRA = {
  "site-internet-vtc": [
    ("Mes clients peuvent-ils réserver pour plus tard ?", "Oui : la réservation se fait à l'avance, avec la date, l'heure, le départ et l'arrivée. C'est d'ailleurs la règle pour un VTC, qui ne peut pas prendre de client sans réservation préalable."),
    ("Puis-je afficher ma carte professionnelle VTC ?", "Oui. Votre numéro de carte et votre inscription au registre peuvent figurer sur le site et dans les mentions légales, ce qui rassure les clients et les hôtels."),
    ("Le site existe-t-il en anglais ?", "Oui, la version anglaise est incluse en formule Premium : utile pour les transferts aéroport et la clientèle d'affaires étrangère.")],
  "site-internet-restaurant": [
    ("Comment indiquer les allergènes ?", "Chaque plat peut afficher ses allergènes, ou le site indique que l'information est disponible sur demande. Les deux façons de faire sont prévues."),
    ("Puis-je recevoir les demandes de groupe et de privatisation ?", "Oui : un formulaire dédié demande la date, le nombre de convives et le budget, et vous répondez avec un devis en PDF depuis votre espace client."),
    ("Combien coûte un site de restaurant ?", "Dès 29 € par mois en Essentiel, plus 190 € de mise en ligne une seule fois, hébergement et nom de domaine compris, sans engagement.")],
  "site-internet-artisan-batiment": [
    ("Puis-je recevoir des photos avec les demandes de devis ?", "Oui : le client joint des photos du chantier au formulaire, ce qui vous aide à estimer avant de vous déplacer."),
    ("Le site parle-t-il des aides comme MaPrimeRénov' ?", "Oui, si vous le souhaitez : une page explique les grandes lignes des aides à la rénovation et précise si vous êtes RGE. Vous la modifiez vous-même quand les règles changent."),
    ("Combien coûte un site pour un artisan ?", "Dès 29 € par mois en Essentiel, plus 190 € de mise en ligne une seule fois, sans engagement.")],
  "site-internet-coiffeur-institut-beaute": [
    ("Puis-je vendre des cartes cadeaux sur le site ?", "Oui : les cartes cadeaux sont présentées sur le site, et la demande arrive chez vous pour que vous la prépariez."),
    ("Mes photos Instagram peuvent-elles apparaître ?", "Oui : le site renvoie vers votre compte Instagram, et vous ajoutez vos plus belles réalisations dans la galerie depuis votre téléphone."),
    ("Combien coûte un site de coiffeur ou d'institut ?", "Dès 29 € par mois en Essentiel, plus 190 € de mise en ligne une seule fois, sans engagement ni commission sur les rendez-vous.")],
  "site-internet-agence-immobiliere": [
    ("Chaque bien a-t-il sa propre page sur Google ?", "Oui : chaque annonce a son adresse, ses photos et ses informations, et Google peut l'indexer comme une page à part entière."),
    ("Puis-je créer des pages pour mes quartiers ?", "Oui : vous ajoutez des pages par commune ou par quartier, qui vous positionnent sur les recherches des vendeurs de votre secteur.")],
}

BODY["site-internet-vtc"].append(("Votre véhicule, votre meilleure vitrine", [
  "Berline, van de 7 ou 8 places, véhicule électrique ou hybride : le client veut voir dans quoi il va voyager. Le site présente votre véhicule en photos, le nombre de passagers et de valises, le confort à bord, et propose le van pour les familles, les groupes et les transferts avec beaucoup de bagages. Pour un mariage ou un événement, une rubrique présente la mise à disposition à l'heure ou à la journée."]))
BODY["site-internet-restaurant"].append(("Raconter votre cuisine", [
  "Votre chef, vos producteurs, vos plats signature, votre cave, votre terrasse : c'est ce qui donne envie de pousser votre porte plutôt que celle d'à côté. Le site leur donne de la place, avec de vraies photos de vos plats et de votre salle, et vous les changez au fil des saisons depuis votre espace client."]))
BODY["site-internet-artisan-batiment"].append(("Les mentions qui rassurent", [
  "Numéro SIRET, assurance décennale avec le nom de l'assureur et la zone couverte, qualifications Qualibat ou RGE, garantie de parfait achèvement : ces mentions sont dans les mentions légales et au pied de chaque page. Pour un particulier qui a déjà entendu parler d'un chantier qui a mal tourné, c'est souvent ce qui fait la différence."]))
BODY["site-internet-coiffeur-institut-beaute"].append(("Vos produits et vos marques", [
  "Les marques que vous utilisez en salon (colorations végétales, soins professionnels, cosmétiques bio) sont un argument pour une partie de la clientèle. Le site les présente, explique pourquoi vous les avez choisies, et signale si elles sont en vente au salon. Une cliente attentive à la composition des produits vous choisira pour ça."]))
BODY["site-internet-agence-immobiliere"].append(("Montrer vos ventes et votre méthode", [
  "Les biens vendus, avec leur délai de vente, prouvent votre efficacité mieux qu'un slogan. Le site garde une rubrique « Vendus » et présente votre méthode : estimation argumentée, photos professionnelles, visites virtuelles, compte rendu après chaque visite, accompagnement jusqu'à l'acte. Un vendeur qui compare plusieurs agences voit tout de suite ce qu'il obtient avec vous."]))
