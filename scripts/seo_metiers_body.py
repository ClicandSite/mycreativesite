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

# 15/11/2026 (Anthony : « fais pareil pour les autres métiers, autant être premier partout ») : tous les métiers à ~1 000 mots
def _add(slug, sections, faq):
    BODY[slug] += sections
    FAQ_EXTRA[slug] = FAQ_EXTRA.get(slug, []) + faq

_add("site-internet-boulangerie", [
  ("Le snacking du midi", [
    "Sandwichs, formules déjeuner, quiches, salades : pour beaucoup de boulangeries, le midi pèse lourd dans la journée. Le site présente vos formules et leurs prix, et les entreprises voisines peuvent passer commande la veille pour un plateau d'équipe. Une demande bien préparée, c'est moins d'attente au comptoir et moins de gâchis.",
    "Vous changez la formule du jour ou de la semaine vous-même, depuis votre téléphone."]),
  ("Vos pains et votre savoir-faire", [
    "Levain naturel, farines Label Rouge ou bio, meunier de la région, fermentation longue, viennoiseries pur beurre : c'est ce qui vous distingue d'un terminal de cuisson. Une page présente votre façon de faire, vos pains du jour et ceux de la semaine (pain de seigle le mardi, brioche le dimanche), pour que les clients sachent quand venir.",
    "Vos récompenses (meilleure baguette du département, concours de galette) y ont leur place."]),
  ("Pâtisserie sur commande", [
    "Entremets, number cakes, pièces montées, gâteaux personnalisés : une galerie montre vos créations et un formulaire demande la date, le nombre de parts et le thème. Ces commandes se préparent plusieurs jours à l'avance, et le site les fait arriver au bon moment."]),
],[
  ("Les clients peuvent-ils commander une bûche ou une galette à l'avance ?", "Oui : ils choisissent le produit, la taille et la date de retrait, et la commande arrive par mail et dans votre espace client."),
  ("Puis-je afficher mes horaires spéciaux pour les fêtes ?", "Oui, vous modifiez vous-même vos horaires et vos fermetures exceptionnelles, qui s'affichent tout de suite sur le site."),
  ("Combien coûte un site pour une boulangerie ?", "Dès 29 € par mois en Essentiel, plus 190 € de mise en ligne une seule fois, hébergement et nom de domaine compris, sans engagement."),
])

_add("site-internet-masseur-osteopathe-bien-etre", [
  ("Une page par soin", [
    "Massage relaxant, modelage aux pierres chaudes, réflexologie plantaire, drainage, soin du dos, séance d'ostéopathie pour adulte, nourrisson ou sportif : chaque soin a sa fiche, avec sa durée, son prix et à qui il s'adresse. Ce sont ces pages précises qui ressortent sur Google quand quelqu'un cherche un soin particulier près de chez lui.",
    "Vous ajoutez un nouveau soin ou une formule de saison vous-même, en quelques minutes."]),
  ("Les entreprises et les événements", [
    "Massage assis en entreprise, ateliers bien-être pour les équipes, présence sur un salon ou un mariage : c'est une clientèle régulière et bien payée. Une rubrique présente ces prestations et reçoit les demandes de devis avec la date, le lieu et le nombre de participants."]),
  ("Ostéopathe : ce que le patient veut savoir", [
    "Durée de la séance, tenue, nombre de séances, remboursement par les mutuelles, prise en charge des nourrissons et des femmes enceintes : le site répond à ces questions en termes simples, sans promesse de guérison. Votre numéro ADELI ou RPPS et votre formation sont indiqués, comme le titre d'ostéopathe le demande."]),
],[
  ("Puis-je proposer des cartes cadeaux ?", "Oui : les cartes cadeaux sont présentées sur le site, et chaque demande arrive chez vous pour que vous l'envoyiez ou la prépariez."),
  ("Combien coûte un site pour un praticien bien-être ou un ostéopathe ?", "Dès 29 € par mois en Essentiel, plus 190 € de mise en ligne une seule fois, sans engagement ni commission sur les séances."),
])

_add("site-internet-concession-moto", [
  ("Une page Google par moto", [
    "Un motard cherche un modèle précis : une MT-07, une Africa Twin, un scooter 125 pour la ville. Chaque moto d'occasion a sa propre page, avec photos, kilométrage, année, entretien, équipements et prix, et Google peut l'indexer. Votre stock travaille pour vous sur des centaines de recherches.",
    "Vous ajoutez et retirez vos motos depuis votre espace client, depuis votre téléphone à l'atelier."]),
  ("Le permis A2 et les jeunes permis", [
    "Les jeunes permis cherchent une moto compatible A2 ou bridable. Le site le signale sur chaque fiche, et une page explique le passage du A2 au A après deux ans. C'est une clientèle qui revient : elle achète une première moto, puis une plus grosse."]),
  ("La saison", [
    "Le printemps fait la saison des ventes, l'hiver celle de l'atelier et du stockage. Le site met en avant ce qui compte au bon moment : vos arrivages et vos essais au printemps, vos forfaits d'hivernage et de révision en automne."]),
],[
  ("Puis-je proposer des essais sur le site ?", "Oui : chaque fiche moto a un bouton pour demander un essai, et la demande arrive chez vous avec les coordonnées du client."),
  ("Mes motos sont-elles diffusées ailleurs que sur mon site ?", "Avec le Pack Auto, Moto & Immo, votre stock est aussi publié sur Abracadeal, sans ressaisie."),
])

_add("site-internet-location-demenagement", [
  ("Particuliers et professionnels", [
    "Un particulier loue un utilitaire pour un week-end ; un artisan a besoin d'un camion benne pour un chantier ; une entreprise déménage ses bureaux. Le site sépare ces clientèles, avec pour chacune vos véhicules ou vos formules adaptées, et un formulaire qui demande les bonnes informations.",
    "Les professionnels peuvent demander une facturation mensuelle ou une location longue durée."]),
  ("Votre flotte en détail", [
    "Volume en mètres cubes, charge utile, permis nécessaire, hayon, nombre de places : chaque véhicule a sa fiche. Le client sait tout de suite quel véhicule choisir pour un studio ou une maison, ce qui évite les erreurs le jour du départ.",
    "Pour les déménagements, présentez vos formules (économique, standard, clés en main) et ce que chacune comprend."]),
  ("Être trouvé au bon moment", [
    "« Location utilitaire » ou « déménageur » suivi d'une ville : ce sont des recherches faites la veille ou la semaine du besoin. Le site affiche votre adresse, vos horaires et un bouton d'appel, et liste les communes que vous couvrez."]),
],[
  ("Les clients peuvent-ils choisir un véhicule précis ?", "Oui : chaque véhicule a sa fiche, et la demande de réservation indique le véhicule souhaité et les dates."),
  ("Puis-je envoyer mes devis depuis le site ?", "Oui : depuis votre espace client, vous éditez un devis en PDF à votre nom pour chaque demande."),
])

_add("site-internet-profession-liberale", [
  ("Une page par domaine d'intervention", [
    "Droit de la famille, droit du travail, création d'entreprise, comptabilité des indépendants, rénovation, conseil en patrimoine : un client cherche une réponse à sa situation, pas un cabinet en général. Chaque domaine a sa page, qui explique les situations courantes et la façon dont vous accompagnez. Ce sont ces pages qui sortent sur Google.",
    "Le ton reste factuel, sans comparaison avec vos confrères ni promesse de résultat."]),
  ("Le premier contact", [
    "Le formulaire demande l'objet de la demande, l'urgence et les documents dont le client dispose. Vous préparez le premier rendez-vous, au cabinet ou en visio, et vous pouvez indiquer vos honoraires pour une première consultation.",
    "Les demandes arrivent par mail et dans votre espace client, confidentielles."]),
  ("Votre parcours", [
    "Formation, années d'expérience, inscription à l'ordre ou à la chambre, langues parlées, associations professionnelles : une page présente votre parcours. Pour une profession de conseil, c'est souvent ce qui décide le client."]),
],[
  ("Puis-je publier des articles sur mon domaine ?", "Oui : vous ajoutez des articles depuis votre espace client. Expliquer les questions fréquentes de vos clients est aussi ce qui vous fait trouver sur Google."),
  ("Les demandes envoyées par le site restent-elles confidentielles ?", "Oui : elles arrivent uniquement dans votre boîte mail et votre espace client, sur une connexion sécurisée."),
])

_add("site-internet-evenementiel", [
  ("Vos formules, clairement", [
    "Formule soirée, formule mariage complet, option cérémonie laïque, location seule ou avec installation : présenter vos formules avec un prix de départ filtre les demandes hors budget et rassure les clients qui n'osent pas demander. Les options (heures en plus, éclairage, machine à fumée, livre d'or photo) s'ajoutent facilement.",
    "Vous modifiez vos formules et vos prix vous-même, d'une saison à l'autre."]),
  ("Les entreprises", [
    "Séminaires, soirées de fin d'année, lancements de produit, inaugurations : les entreprises réservent plus tôt, ont des budgets plus élevés et reviennent chaque année. Une rubrique leur est dédiée, avec vos références et une demande de devis adaptée (nombre de participants, lieu, horaires)."]),
  ("Les avis et les références", [
    "Les couples et les entreprises lisent les avis avant de choisir. Le site renvoie vers vos avis Google et présente quelques témoignages de clients, avec leur accord, ainsi que les lieux de réception où vous avez déjà travaillé."]),
],[
  ("Puis-je indiquer les dates où je ne suis plus disponible ?", "Oui : vous signalez vos dates déjà réservées, et le formulaire invite le client à donner une date de repli."),
  ("Le site convient-il à un loueur de matériel événementiel ?", "Oui : chaque article (tentes, mobilier, sonorisation, décoration) a sa fiche avec ses photos et son prix de location."),
])

_add("site-internet-tourisme-loisirs", [
  ("Une page par activité", [
    "Sortie demi-journée, journée complète, coucher de soleil, initiation, sortie privée : chaque activité a sa page avec les photos, le programme heure par heure, le niveau, le prix et le lieu de rendez-vous. Les visiteurs qui cherchent une activité précise tombent sur la bonne page, pas sur un catalogue.",
    "Vous pouvez aussi présenter des idées pour les familles, les couples ou les groupes d'amis."]),
  ("Cartes cadeaux et réservations hors saison", [
    "Une sortie en kayak ou un baptême de parapente, c'est un cadeau très demandé. Les cartes cadeaux vendues en hiver remplissent vos créneaux du printemps. Le site les présente toute l'année."]),
  ("Votre région, votre terrain", [
    "Parlez de votre coin : les sentiers, les spots, les villages, la faune. Ces textes donnent envie, montrent que vous connaissez le terrain, et sont aussi lus par Google, qui associe votre site à votre région."]),
],[
  ("Puis-je proposer des cartes cadeaux ?", "Oui : elles sont présentées sur le site, et chaque demande arrive chez vous pour que vous l'envoyiez au client."),
  ("Le site gère-t-il les groupes et les écoles ?", "Oui : une demande de devis dédiée recueille le nombre de participants, l'âge et la date souhaitée."),
])

_add("site-internet-traiteur", [
  ("Mariages et grandes réceptions", [
    "Pour un mariage, le couple veut savoir ce qui est compris : cocktail, entrée, plat, dessert, pièce montée, service, vaisselle, mobilier, nappage. Une rubrique détaille vos formules de réception et propose une dégustation sur rendez-vous. C'est souvent ce qui fait la différence avec un concurrent qui envoie seulement un prix."]),
  ("Votre cuisine et vos produits", [
    "Produits frais, circuits courts, fait maison, spécialités régionales ou du monde : présentez ce qui vous distingue, avec de vraies photos de vos buffets et de vos plats. Les clients choisissent un traiteur sur ses photos autant que sur ses prix.",
    "Vous changez vos menus de saison vous-même depuis votre espace client."]),
  ("Livraison et service", [
    "Livraison seule, installation du buffet, maîtres d'hôtel, reprise de la vaisselle : le site présente ce que vous proposez et votre zone d'intervention, avec les éventuels frais de déplacement. Le client sait à quoi s'attendre avant de demander un devis."]),
],[
  ("Puis-je proposer une dégustation avant un mariage ?", "Oui : une demande de dégustation peut être faite depuis le site, et vous fixez le rendez-vous avec le couple."),
  ("Le site convient-il à un traiteur qui fait aussi de la vente en boutique ?", "Oui : la boutique a sa rubrique avec ses horaires et ses plats du jour, à côté de l'activité réception."),
])

_add("site-internet-photographe", [
  ("Vos tarifs, sans détour", [
    "Les clients hésitent à contacter un photographe qui n'affiche aucun prix. Présentez vos formules avec un prix de départ : séance portrait, séance famille, reportage mariage à la demi-journée ou à la journée, prise de vue pour entreprise. Le client arrive en sachant si vous êtes dans son budget, et vous perdez moins de temps.",
    "Les options (album, tirages, séance d'engagement) s'ajoutent à chaque formule."]),
  ("Le déroulé d'une séance", [
    "Où se passe la séance, combien de temps, comment se préparer, quand arrivent les photos, comment elles sont livrées : une page explique le déroulé, ce qui rassure ceux qui n'ont jamais été photographiés par un professionnel."]),
  ("Les entreprises", [
    "Portraits d'équipe, photos de locaux, produits, événements, photos immobilières : les entreprises ont besoin d'images régulièrement. Une rubrique présente vos prestations pour elles, avec la question des droits d'utilisation réglée dès le devis."]),
],[
  ("Puis-je livrer les photos à mes clients depuis le site ?", "Le site présente votre portfolio ; pour la livraison, vous continuez d'utiliser votre outil de galerie privée, et le site peut y renvoyer."),
  ("Le site peut-il être en anglais pour les mariages de couples étrangers ?", "Oui, la version anglaise est incluse en formule Premium."),
])

_add("site-internet-location-bateau", [
  ("Une fiche par bateau", [
    "Semi-rigide, bateau à moteur, voilier, catamaran, jet-ski, paddle : chaque embarcation a sa fiche avec ses photos, sa capacité, sa puissance, l'équipement à bord (taud de soleil, échelle de bain, glacière) et ses tarifs à la demi-journée, à la journée ou à la semaine. Le client choisit en connaissance de cause.",
    "Vous ajoutez et retirez vos bateaux vous-même au fil des saisons."]),
  ("Le skipper, un service à part", [
    "Beaucoup de clients n'ont pas le permis ou préfèrent profiter sans piloter. Une rubrique présente vos sorties avec skipper : balade, journée aux îles, coucher de soleil, demande en mariage, anniversaire. Ce sont des prestations à forte valeur, très recherchées."]),
  ("Préparer la sortie", [
    "Heure d'arrivée, documents à présenter, briefing de sécurité, ce qu'il faut apporter, où se garer : une page explique tout avant le départ. Les clients arrivent prêts, et les départs se font à l'heure."]),
],[
  ("Puis-je demander une caution ?", "Oui : le montant de la caution et ses conditions sont indiqués sur chaque fiche et dans vos conditions de location."),
  ("Le site convient-il aux sorties avec skipper ?", "Oui : chaque sortie avec skipper a sa page, avec son programme, sa durée et son prix."),
])

_add("site-internet-services-a-domicile", [
  ("Un service par page", [
    "Ménage régulier, grand ménage de printemps, repassage, jardinage, petit bricolage, garde d'enfants après l'école, aide aux courses : chaque service a sa page avec ce qui est compris, la fréquence possible et le prix horaire après crédit d'impôt. Les familles qui cherchent un service précis trouvent la bonne page.",
    "Vous ajoutez un nouveau service vous-même, par exemple un service de saison."]),
  ("Comment se passe le premier rendez-vous", [
    "Visite à domicile ou appel, devis gratuit, choix de l'intervenant, jour et horaire fixes, remplacement en cas d'absence, facture et attestation fiscale chaque année : expliquer ces étapes rassure les clients qui n'ont jamais fait appel à une entreprise de services à domicile."]),
  ("Les seniors et leurs proches", [
    "Souvent, ce n'est pas la personne âgée qui cherche, mais son fils ou sa fille, parfois loin. Une rubrique s'adresse à eux : services proposés, suivi, contact direct avec l'intervenant, aides possibles (APA, caisses de retraite)."]),
],[
  ("Le site explique-t-il l'attestation fiscale ?", "Oui : il rappelle que vous envoyez chaque année une attestation pour le crédit d'impôt, si vous êtes déclaré en services à la personne."),
  ("Puis-je recruter des intervenants via le site ?", "Oui : une page « Nous rejoindre » peut recevoir les candidatures, qui arrivent par mail."),
])

_add("site-internet-fleuriste", [
  ("La boutique en ligne de vos créations", [
    "Bouquets du moment, bouquets de saison, compositions, plantes, orchidées : chaque création a sa photo, son prix et ses tailles. Vous changez la vitrine chaque semaine depuis votre téléphone, avec les fleurs arrivées le matin.",
    "Le client précise le message de la carte, la date et l'adresse de livraison."]),
  ("Votre zone de livraison", [
    "Le site indique les communes livrées, les frais selon la distance et l'heure limite de commande pour une livraison le jour même. Les clients qui envoient des fleurs à un proche dans votre ville vous trouvent sur Google, même s'ils habitent loin."]),
  ("Votre style", [
    "Champêtre, moderne, fleurs locales et de saison, fleurs séchées, zéro plastique : présentez votre style et vos engagements. Une clientèle de plus en plus nombreuse choisit son fleuriste pour ça."]),
],[
  ("Les clients peuvent-ils écrire un message pour la carte ?", "Oui : le formulaire de commande prévoit le texte de la carte, la date et l'adresse de livraison."),
  ("Puis-je indiquer une heure limite pour la livraison du jour ?", "Oui, elle est affichée sur le site et vous la modifiez vous-même."),
])

_add("site-internet-infirmier-liberal", [
  ("Les informations pratiques", [
    "Adresse du cabinet, accès, parking, accessibilité, horaires de permanence, documents à préparer (ordonnance, carte Vitale, attestation de mutuelle) : une page réunit tout ce dont le patient a besoin avant le premier soin.",
    "Vous les modifiez vous-même, par exemple pendant les congés ou les remplacements."]),
  ("Les soins après une hospitalisation", [
    "La sortie d'hôpital ou de clinique est un moment où les familles cherchent un infirmier en urgence : pansements, injections d'anticoagulants, retrait des fils, surveillance. Une rubrique explique comment organiser la prise en charge avant la sortie, pour que le patient ne se retrouve pas sans soins le premier jour."]),
  ("Le bilan de soins infirmiers", [
    "Pour les patients âgés ou dépendants, le site peut expliquer le bilan de soins infirmiers et les soins d'hygiène à domicile, en lien avec le médecin traitant. Les proches comprennent ce qui est possible et à qui s'adresser."]),
],[
  ("Puis-je indiquer mes communes de tournée ?", "Oui : le site liste vos communes, et le patient sait tout de suite si vous intervenez chez lui."),
  ("Le site convient-il à un remplaçant ?", "Oui : vous pouvez présenter les infirmiers du cabinet et les remplaçants réguliers."),
])

_add("site-internet-toiletteur", [
  ("Les prestations, une par une", [
    "Bain et séchage, tonte, coupe ciseaux, épilation, démêlage, coupe des griffes, nettoyage des oreilles, toilettage du chat : chaque prestation a sa description, sa durée et son prix par gabarit. Le client sait ce qu'il réserve et combien il va payer.",
    "Les forfaits chiot, pour habituer le jeune chien au toilettage, ont leur page."]),
  ("Le bien-être de l'animal", [
    "Les propriétaires veulent savoir comment leur animal est traité : temps d'attente, séchage, manipulation des chiens anxieux ou âgés, produits utilisés. Expliquer votre façon de faire rassure et fidélise."]),
  ("Les races et les coupes", [
    "Une page par type de pelage (chiens à poils longs, bouclés, à double pelage) explique ce qu'il faut et à quelle fréquence. Ces pages répondent aux questions des propriétaires et sortent sur Google sur des recherches précises."]),
],[
  ("Puis-je afficher mes tarifs par race ?", "Oui : vos tarifs sont présentés par gabarit ou par race, et vous les modifiez vous-même."),
  ("Le site accepte-t-il les chats ?", "Oui : vous présentez vos prestations pour chats et NAC si vous les proposez."),
])

_add("site-internet-coach-sportif", [
  ("Une page par programme", [
    "Remise en forme, perte de poids, renforcement musculaire, préparation à une course, coaching prénatal ou postnatal, sport après 60 ans : chaque programme a sa page avec son public, son déroulé et son tarif. Le client se reconnaît dans une situation précise.",
    "Vous ajoutez un nouveau programme ou un stage vous-même."]),
  ("Les cours collectifs", [
    "Cours en extérieur, bootcamp, pilates, cross-training en petit groupe : le planning est affiché sur le site, avec le lieu, le niveau et le nombre de places. Les demandes d'inscription arrivent chez vous."]),
  ("Les entreprises", [
    "Séances pour les salariés, ateliers de prévention du mal de dos, défis sportifs : une rubrique présente vos offres pour les entreprises, une clientèle régulière qui paie bien."]),
],[
  ("Puis-je publier mon planning de cours ?", "Oui : vous le modifiez vous-même chaque semaine depuis votre espace client."),
  ("Puis-je afficher ma carte professionnelle ?", "Oui : votre carte d'éducateur sportif et vos diplômes figurent sur le site, ce qui rassure les clients."),
])

_add("site-internet-chambres-d-hotes-gite", [
  ("Votre table d'hôtes et vos services", [
    "Table d'hôtes, panier pique-nique, location de vélos, piscine, spa, accueil des randonneurs ou des cyclistes : présentez ce qui rend votre maison unique, avec les prix et les jours de service. Ce sont souvent ces détails qui font choisir une maison d'hôtes plutôt qu'un hôtel."]),
  ("Les séjours à thème et les groupes", [
    "Week-end en amoureux, séjour vendanges, réunion de famille, petit séminaire : proposez des séjours à thème et la location de toute la maison. Ces demandes arrivent rarement par les plateformes et rapportent plus."]),
  ("Les informations pratiques", [
    "Heure d'arrivée et de départ, accès, parking, animaux, enfants, conditions d'annulation, acompte : une page claire évite les malentendus et les messages répétés. Vous la modifiez vous-même à chaque saison."]),
],[
  ("Puis-je proposer la location de toute la maison ?", "Oui : une rubrique dédiée reçoit les demandes de groupe, avec les dates et le nombre de personnes."),
  ("Puis-je indiquer mes périodes de fermeture ?", "Oui, vous les signalez vous-même et elles s'affichent sur le site."),
])

_add("site-internet-auto-ecole", [
  ("Les tarifs détaillés", [
    "Forfait code, forfait 20 heures, heure supplémentaire, présentation à l'examen, accompagnement, frais d'inscription : afficher vos tarifs en détail est une obligation pour une auto-école et un vrai argument face aux offres qui cachent les frais. Le site présente chaque formule clairement.",
    "Vous modifiez vos tarifs vous-même à chaque changement."]),
  ("Les élèves et leurs parents", [
    "Souvent, ce sont les parents qui choisissent et qui paient. Une rubrique leur répond : conduite accompagnée, rendez-vous pédagogiques, financement (CPF, permis à 1 € par jour, aides locales), suivi de la progression. Rassurer les parents, c'est gagner l'inscription."]),
  ("Les formations pour adultes", [
    "Reprise de conduite après une longue pause, perfectionnement, conduite en boîte automatique, stage de récupération de points : les adultes cherchent aussi une auto-école. Une page par formation leur répond directement."]),
],[
  ("Le site peut-il expliquer le financement par le CPF ?", "Oui : une page explique les grandes lignes et précise si vos formations sont éligibles."),
  ("Puis-je présenter mes moniteurs ?", "Oui : chaque moniteur peut être présenté avec sa photo et ses spécialités."),
])

_add("site-internet-bijouterie", [
  ("Vos créations et vos marques", [
    "Bagues, colliers, boucles d'oreilles, alliances, montres : présentez vos collections en photo, avec un prix de départ si vous le souhaitez, sans vendre en ligne. Le client repère les pièces qui lui plaisent et vient les voir en boutique.",
    "Vous ajoutez vos nouveautés vous-même, depuis votre téléphone."]),
  ("L'atelier", [
    "Si vous avez un atelier, montrez-le : bijoutier ou horloger au travail, outils, savoir-faire, délais. Un client confie plus volontiers une montre de famille ou une bague ancienne à quelqu'un dont il voit le travail."]),
  ("Les alliances", [
    "Les couples cherchent leurs alliances plusieurs mois avant le mariage, souvent sur Google. Une page dédiée présente vos modèles, les métaux, la gravure, le délai de fabrication, et propose un rendez-vous au calme."]),
],[
  ("Puis-je présenter mes services de réparation avec un délai ?", "Oui : chaque service (pile, révision, mise à taille, soudure) peut afficher un délai et un prix indicatifs."),
  ("Puis-je proposer des rendez-vous privés ?", "Oui : un formulaire permet de demander un rendez-vous, par exemple pour choisir des alliances."),
])

_add("site-internet-concession-automobile", [
  ("Utilitaires et professionnels", [
    "Artisans, livreurs, entreprises : les véhicules utilitaires ont leur rubrique, avec le volume, la charge utile, les aménagements et les solutions de location avec option d'achat. C'est une clientèle qui revient régulièrement renouveler sa flotte."]),
  ("L'après-vente", [
    "Révision, entretien sous garantie, pneus, carrosserie, contrôle technique : si vous avez un atelier, le site prend les rendez-vous. Un client bien suivi après l'achat revient acheter son prochain véhicule chez vous."]),
  ("Être trouvé sur les modèles recherchés", [
    "Les acheteurs tapent un modèle, une motorisation et une ville. Avec une page par véhicule et des informations complètes (finition, options, Crit'Air, consommation), vos voitures sortent sur ces recherches précises, pas seulement sur le nom de votre concession."]),
],[
  ("Puis-je afficher la vignette Crit'Air et la consommation ?", "Oui : chaque fiche véhicule prévoit ces informations, utiles aux acheteurs dans les villes à zone à faibles émissions."),
  ("Le site prend-il les rendez-vous atelier ?", "Oui : la prise de rendez-vous pour l'entretien et la révision est incluse."),
])

_add("site-internet-dentiste", [
  ("Les actes, expliqués simplement", [
    "Détartrage, soins de caries, dévitalisation, couronne, bridge, implant, blanchiment, orthodontie : une page explique chaque acte en termes simples, combien de temps il prend, combien de séances il faut, et s'il est pris en charge. Les patients arrivent mieux informés, et moins inquiets.",
    "Le contenu reste informatif, comme le demande le code de déontologie."]),
  ("Les enfants et les patients anxieux", [
    "Le dispositif M'T dents, le premier rendez-vous d'un enfant, l'accueil des patients qui ont peur du dentiste : si votre cabinet y fait attention, le site le dit. C'est souvent ce que cherchent les parents."]),
  ("Le cabinet", [
    "Équipe, assistantes, équipements (radiographie numérique, empreinte optique), protocoles d'hygiène et de stérilisation : une page présente le cabinet avec des photos. Elle rassure avant la première visite."]),
],[
  ("Le site peut-il expliquer le 100 % Santé ?", "Oui : une page présente les grandes lignes du 100 % Santé dentaire et rappelle qu'un devis est remis avant toute prothèse."),
  ("Puis-je indiquer si je prends de nouveaux patients ?", "Oui, et vous modifiez cette information vous-même selon vos disponibilités."),
])

_add("site-internet-veterinaire", [
  ("Une page par service", [
    "Consultation, vaccination, chirurgie, dentisterie, imagerie, analyses, hospitalisation, comportement, NAC : chaque service a sa page qui explique ce qui est fait et quand consulter. Les propriétaires qui cherchent un service précis tombent sur la bonne page.",
    "Vous ajoutez un nouveau service vous-même."]),
  ("Les chiots et les chatons", [
    "Premiers vaccins, identification, vermifuges, stérilisation, alimentation, éducation : une rubrique accompagne les nouveaux propriétaires. C'est une clientèle qui reste fidèle pendant toute la vie de l'animal."]),
  ("Les animaux âgés", [
    "Bilans de santé, douleur, arthrose, alimentation adaptée, accompagnement de fin de vie : une page traite ces sujets avec délicatesse. Les propriétaires y trouvent des réponses et savent qu'ils peuvent compter sur vous."]),
],[
  ("Puis-je présenter les services de garde ?", "Oui : le site indique votre organisation pour les urgences et le service de garde vers lequel vous orientez."),
  ("Le site convient-il à une clinique avec plusieurs vétérinaires ?", "Oui : chaque vétérinaire est présenté avec ses domaines d'intérêt."),
])

_add("site-internet-kinesitherapeute", [
  ("Les sportifs", [
    "Entorse, tendinite, rupture des ligaments croisés, reprise après blessure, prévention : les sportifs cherchent un kinésithérapeute qui comprend leur pratique. Si c'est votre cas, une page le présente, avec votre approche de la reprise progressive."]),
  ("Les enfants et les nourrissons", [
    "Kinésithérapie respiratoire, troubles orthopédiques, développement moteur : si vous recevez des enfants, une rubrique l'explique aux parents, avec les situations où consulter et la façon dont se passent les séances."]),
  ("Les informations pratiques", [
    "Durée d'une séance, tenue, documents, annulation, retard, remplacements pendant les congés : une page réunit ces informations et vous évite les questions répétées au téléphone."]),
],[
  ("Puis-je présenter les remplaçants du cabinet ?", "Oui : chaque praticien et remplaçant régulier peut être présenté."),
])

# Dernière section par métier, pour dépasser les 1 000 mots
_LAST = {
 "site-internet-concession-moto": ("Équipement et accessoires", "Casques, blousons, gants, bottes, antivols, bagagerie, intercoms : l'équipement représente une part importante du chiffre d'une concession. Le site présente les marques que vous distribuez et vos conseils pour bien choisir sa taille ou son niveau de protection, avec un rendez-vous pour l'essayage. Les motards qui cherchent un casque ou un blouson près de chez eux vous trouvent sur Google, et repartent souvent avec plus que ce qu'ils étaient venus chercher. Vos événements (portes ouvertes, balades, essais de nouveaux modèles) ont aussi leur place, et fidélisent votre clientèle locale."),
 "site-internet-tourisme-loisirs": ("Sécurité et conditions", "Âge minimum, poids maximum, savoir nager, condition physique, femmes enceintes, conditions météo, annulation et report : une page claire répond à ces questions avant la réservation. Elle évite les mauvaises surprises au point de rendez-vous et montre votre sérieux. Indiquez aussi ce qui est fourni (combinaison, casque, gilet, matériel) et ce qu'il faut apporter (chaussures fermées, crème solaire, eau). Les familles, en particulier, choisissent l'activité qui répond le plus clairement à leurs questions, et elles sont nombreuses à préparer leurs vacances depuis leur canapé, des semaines à l'avance."),
 "site-internet-coach-sportif": ("Le bilan de départ", "Un premier rendez-vous bien mené fait souvent la différence entre un prospect et un client. Le site explique comment se passe votre bilan : objectifs, antécédents, tests de condition physique, mensurations si le client le souhaite, puis un programme adapté. Il propose de réserver ce bilan directement, gratuit ou payant selon votre choix. Les clients qui hésitent à se lancer, souvent parce qu'ils n'ont pas fait de sport depuis longtemps, sont rassurés de voir qu'on part de leur niveau réel, sans jugement. C'est aussi l'occasion d'expliquer le suivi entre les séances : conseils, ajustements, messages."),
 "site-internet-evenementiel": ("Le déroulé de A à Z", "Premier contact, rendez-vous ou appel pour comprendre l'événement, devis détaillé, acompte, réunion de préparation, repérage du lieu, jour J, bilan : expliquer votre façon de travailler rassure, surtout pour un mariage où tout doit être parfait. Le site présente ces étapes simplement, avec les délais habituels et ce que vous attendez du client à chaque moment. Les couples et les organisateurs d'entreprise comparent souvent plusieurs prestataires : celui qui montre qu'il a une méthode, des contrats clairs et un plan B en cas d'imprévu se démarque nettement."),
 "site-internet-profession-liberale": ("Honoraires et transparence", "Beaucoup de clients hésitent à contacter un professionnel par peur du coût. Le site peut présenter votre mode de facturation : forfait pour certaines missions, taux horaire, convention d'honoraires, provision, aide juridictionnelle ou dispositifs d'aide quand ils existent dans votre profession. Sans donner un prix pour chaque situation, expliquer comment vous facturez lève un frein important. Les mentions obligatoires de votre profession sur ce point sont respectées, et vous gardez la main sur ces textes depuis votre espace client, pour les mettre à jour quand vos conditions évoluent."),
 "site-internet-masseur-osteopathe-bien-etre": ("Votre cabinet, votre ambiance", "Lumière, musique, huiles, linge, table chauffante, espace douche : pour un soin bien-être, l'ambiance fait partie de la prestation. Le site la montre en photos et décrit le moment que le client va vivre, de l'accueil au thé servi après la séance. Pour un ostéopathe, l'accent est mis sur le sérieux : salle de soins, accessibilité, horaires élargis le soir ou le samedi. Dans les deux cas, l'adresse, le plan, le parking et les transports sont affichés clairement, car la plupart des clients consultent le site depuis leur téléphone juste avant de partir."),
 "site-internet-fleuriste": ("Les entreprises et les événements", "Abonnement floral pour l'accueil d'un hôtel ou d'un cabinet, décoration d'un séminaire, fleurs pour un restaurant, compositions pour un salon : les entreprises sont une clientèle régulière et fidèle. Une rubrique leur présente vos formules, avec une fréquence de livraison et un budget mensuel, et reçoit leurs demandes de devis. Pour les mariages et les événements privés, une galerie de vos décorations de table, d'arches et de bouquets de mariée aide les futurs mariés à se projeter. Ces demandes arrivent par mail et dans votre espace client, où vous suivez chaque devis."),
 "site-internet-chambres-d-hotes-gite": ("Ce que disent vos hôtes", "Les voyageurs lisent les avis avant de réserver. Le site renvoie vers vos avis Google et peut reprendre, avec leur accord, quelques mots de vos hôtes. Il présente aussi votre histoire : pourquoi vous avez ouvert votre maison, ce que vous aimez faire découvrir, vos adresses préférées. C'est ce lien personnel que les voyageurs viennent chercher dans une maison d'hôtes, et que les plateformes ne savent pas montrer. Pour les gîtes, un livret d'accueil en ligne (wifi, tri des déchets, commerces, numéros utiles) évite bien des questions pendant le séjour."),
 "site-internet-toiletteur": ("La boutique et les conseils", "Shampoings, brosses, produits anti-parasitaires, accessoires, friandises : si vous vendez des produits, le site les présente avec vos conseils d'utilisation. Une rubrique conseils répond aux questions fréquentes : à quelle fréquence brosser, comment éviter les nœuds, que faire après une baignade, comment couper les griffes sans blesser. Ces pages font revenir les clients entre deux toilettages, sont lues par Google et montrent votre expertise. Vous les rédigez avec vos mots depuis votre espace client, et vous pouvez y ajouter vos photos."),
 "site-internet-location-demenagement": ("Les conseils pour bien déménager", "Combien de cartons pour un deux-pièces, comment protéger la vaisselle, quel volume pour une maison, quelles démarches faire avant de partir (changement d'adresse, résiliation, état des lieux, autorisation de stationnement) : une rubrique conseils aide vos clients et leur montre votre expérience. Ces pages sont très recherchées sur Google pendant la préparation d'un déménagement, bien avant la réservation. Elles amènent des visiteurs qui, une fois rassurés, vous demandent un devis. Vous pouvez aussi y présenter vos fournitures : cartons, papier bulle, adhésif, housses."),
 "site-internet-photographe": ("Votre regard", "Ce qui fait choisir un photographe, au-delà du prix, c'est son regard : naturel, lumineux, documentaire, artistique, noir et blanc. Une page « À propos » raconte votre parcours, ce que vous aimez photographier et ce que vos clients disent de vous. Elle montre aussi votre visage : on choisit plus facilement quelqu'un qu'on a déjà vu, surtout pour une journée aussi importante qu'un mariage. Vos parutions, expositions ou récompenses complètent la présentation et rassurent les clients exigeants."),
 "site-internet-location-bateau": ("Vos idées de sorties", "Où aller pour une demi-journée, quelle crique choisir selon le vent, où mouiller pour déjeuner, quels lieux protégés respecter : une page de suggestions d'itinéraires aide vos clients à profiter de leur sortie et montre votre connaissance du plan d'eau. Elle est aussi très lue par les vacanciers qui préparent leur séjour. Ajoutez vos conseils de sécurité (météo, zones interdites, distances à respecter des plages) : vos clients partent mieux préparés, et vos bateaux reviennent en bon état."),
 "site-internet-auto-ecole": ("Le code de la route", "Salle de code, tests en ligne, sessions de révision encadrées, inscription à l'examen du code : présentez comment vous préparez vos élèves à l'épreuve théorique. Beaucoup d'élèves révisent seuls sur une application ; votre accompagnement en salle et vos conseils font la différence le jour de l'examen. Le site indique vos horaires de salle de code et vos sessions de révision intensive pendant les vacances scolaires, une période où les inscriptions affluent. Les demandes d'inscription arrivent directement chez vous, sans plateforme intermédiaire."),
 "site-internet-kinesitherapeute": ("Les seniors et le maintien à domicile", "Prévention des chutes, rééducation après une fracture, maintien de la mobilité, accompagnement des maladies chroniques : les patients âgés et leurs proches cherchent un kinésithérapeute disponible et proche, parfois à domicile. Une rubrique leur explique ce qui est possible, sur prescription du médecin, et comment organiser les séances. Les proches, souvent à distance, y trouvent les informations utiles et un moyen simple de vous contacter, ce qui facilite la mise en place des soins."),
 "site-internet-infirmier-liberal": ("Les vaccinations et les prélèvements", "Vaccination contre la grippe ou le Covid, prises de sang à domicile ou au cabinet, tests : ces soins sont très recherchés à certaines périodes de l'année. Le site indique ce que vous faites, sur quelles plages horaires, et s'il faut une ordonnance. En période de campagne de vaccination, une simple mise à jour depuis votre espace client permet d'afficher vos créneaux et d'éviter des dizaines d'appels. Les patients savent où et quand venir, et le cabinet reste joignable pour les urgences."),
 "site-internet-bijouterie": ("Le rachat et l'estimation", "Bijoux hérités, or cassé, montres anciennes : beaucoup de personnes ne savent pas ce que valent leurs objets et hésitent à pousser la porte d'un comptoir. Le site explique comment se passe une estimation dans votre boutique, ce que vous rachetez, comment le prix est calculé selon le cours de l'or, et les documents à apporter. Cette transparence attire une clientèle qui ne serait jamais venue autrement, et qui revient souvent ensuite pour acheter ou faire transformer une pièce."),
 "site-internet-traiteur": ("Les fêtes de fin d'année", "Foie gras, plateaux de fruits de mer, bûches, menus de réveillon, buffets d'entreprise : la fin d'année concentre une grande partie des commandes. Le site met en avant votre carte de fêtes dès novembre, avec les dates limites de commande et les créneaux de retrait. Les clients commandent tranquillement à l'avance, et vous organisez votre production sans être débordé les derniers jours. Après les fêtes, vous remettez votre carte habituelle en quelques minutes depuis votre espace client."),
 "site-internet-services-a-domicile": ("Des intervenants de confiance", "Recrutement, vérifications, formation, assurance, encadrement : expliquer comment vous choisissez et suivez vos intervenants rassure les clients qui vont leur confier les clés de leur maison ou leurs enfants. Le site peut présenter votre équipe, la façon dont un intervenant attitré est désigné, et ce qui se passe s'il est absent ou si le client souhaite changer. C'est l'argument principal face aux particuliers non déclarés, et ce que les familles comparent en premier."),
 "site-internet-boulangerie": ("Vos engagements", "Farine locale, produits de saison, fait maison, lutte contre le gaspillage (dons, invendus à prix réduit en fin de journée), emballages réduits : les clients sont de plus en plus attentifs à ces engagements. Le site les présente simplement, avec des photos de votre fournil et de votre équipe. Les recherches « boulangerie artisanale » ou « pain au levain » suivies d'un quartier sont fréquentes : une page qui parle de votre façon de travailler vous fait apparaître sur ces recherches, devant les chaînes."),
 "site-internet-concession-automobile": ("La reprise, première étape de la vente", "La plupart des acheteurs ont un véhicule à revendre. Le formulaire de reprise du site demande la marque, le modèle, l'année, le kilométrage, l'état et des photos : vous faites une première estimation avant le rendez-vous, et le client sait que la reprise est possible chez vous. C'est souvent ce qui déclenche la visite en concession. Les demandes arrivent dans votre espace client, où vous suivez chaque dossier jusqu'à la vente."),
 "site-internet-veterinaire": ("Les conseils de saison", "Chenilles processionnaires au printemps, coups de chaleur en été, épillets, tiques, intoxications de fin d'année : une rubrique de conseils de saison aide les propriétaires à protéger leur animal et leur rappelle quand consulter. Ces pages sont très recherchées sur Google au bon moment, et elles amènent de nouveaux clients vers votre clinique. Vous les rédigez ou les complétez vous-même depuis votre espace client, avec les particularités de votre région."),
 "site-internet-dentiste": ("Accès et informations pratiques", "Adresse, étage, ascenseur, accès en fauteuil roulant, parking, transports en commun, horaires, moyens de paiement, tiers payant, annulation d'un rendez-vous : une page réunit ces informations et évite des appels au secrétariat. Elle est d'autant plus utile que les patients la consultent souvent juste avant de partir, depuis leur téléphone. Vous la mettez à jour vous-même pendant les congés ou en cas de changement d'horaires."),
}
for _s, (_h, _t) in _LAST.items():
    BODY[_s].append((_h, [_t]))

# 22/11/2026 (tâche de nuit) : photographe, droit à l'image (source : service-public.gouv.fr F32103, CNIL)
_add("site-internet-photographe", [
  ("Votre portfolio et le droit à l'image", [
    "Votre portfolio montre des gens : des mariés, des familles, des enfants, des salariés. Avant de publier une photo où une personne est reconnaissable, il faut son accord écrit. Le fait qu'elle ait accepté d'être photographiée ne suffit pas.",
    "L'accord doit être précis : sur quel support la photo sera publiée (votre site, vos réseaux), dans quel but et pour combien de temps. Le plus simple est de prévoir une case ou une clause dans votre contrat ou votre devis, que le client remplit dès la réservation.",
    "Pour un enfant, c'est l'accord écrit des parents qu'il faut. Pour une photo de groupe d'enfants, l'accord des parents de chaque enfant.",
    "Si un client refuse, rien ne vous empêche de montrer votre travail autrement : détails, décor, mains, silhouettes de dos, paysages ou objets. Et si un client change d'avis plus tard, vous retirez la photo vous-même depuis votre espace client, en quelques secondes."]),
],[
  ("Puis-je mettre les photos de mes clients dans mon portfolio en ligne ?", "Oui, avec leur accord écrit et précis (support, but, durée) pour chaque personne reconnaissable, et celui des parents pour un enfant. Prévoyez-le dans votre contrat dès la réservation."),
])

# 16/11/2026 (passage SEO) : pages d'intention et page Cannes enrichies.
# BODY_EXTRA s'ajoute à la fin d'un « body » existant (pages déjà enrichies dans seo_contenu.py).
BODY_EXTRA = {
 "site-internet-auto-entrepreneur": [
  ("Un site, une charge que vous ne déduisez pas", [
    "En micro-entreprise, vous ne déduisez pas vos frais réels : vos cotisations et votre impôt sont calculés sur votre chiffre d'affaires, après un abattement forfaitaire. Chaque euro dépensé pour le site sort donc directement de votre poche. C'est pour ça qu'une formule mensuelle modeste, sans gros chèque au départ et sans engagement, est souvent plus adaptée qu'un site à plusieurs milliers d'euros.",
    "Le calcul est simple : si un seul client par mois vous trouve grâce à votre site, l'abonnement est en général largement remboursé."]),
  ("Mieux que les plateformes pour se faire connaître", [
    "Les plateformes de mise en relation et les annuaires sont utiles pour démarrer, mais elles prennent souvent une commission et mettent vos concurrents juste à côté de vous. Votre site, lui, ne parle que de vous. Il sert de carte de visite quand un client potentiel cherche votre nom après vous avoir croisé, et c'est l'adresse que vous mettez sur vos devis, vos factures et vos réseaux sociaux.",
    "Gardez les plateformes si elles vous apportent des clients, et faites de votre site le lieu où les clients satisfaits reviennent vous chercher."]),
  ("Démarrer petit, grandir ensuite", [
    "Vous commencez avec la formule Essentiel et le modèle de votre métier. Si votre activité décolle, vous passez en Pro pour encaisser des acomptes en ligne, ou en Premium pour gérer vos clients et avoir un site en anglais : votre site, vos textes et votre nom de domaine restent les mêmes, rien n'est à refaire. Et si vous changez de statut, en passant en société par exemple, il suffit de mettre à jour vos mentions légales."]),
 ],
 "site-internet-creation-entreprise": [
  ("Réserver son nom de domaine en même temps que son nom", [
    "Le nom de votre entreprise et votre nom de domaine vont ensemble. Avant de valider votre nom, vérifiez que l'adresse en .fr est libre, et réservez-la tout de suite : quelques euros par an suffisent, et ça évite de devoir choisir un nom de site différent de votre enseigne. Vérifiez aussi auprès de l'INPI que le nom n'est pas déjà protégé par une marque dans votre secteur.",
    "Avec MyCreativeSite, le nom de domaine est compris dans l'abonnement et enregistré à votre nom."]),
  ("Les 90 premiers jours", [
    "Les premiers mois, votre site sert surtout à rassurer : un client qui hésite à faire appel à une entreprise toute neuve vérifie qu'elle existe vraiment. Des coordonnées complètes, des prix clairs, des photos de vos premières réalisations et vos premiers avis font plus que n'importe quel slogan.",
    "Pensez à ajouter chaque nouvelle réalisation au fil de l'eau depuis votre téléphone : en trois mois, votre site aura l'air d'une entreprise installée."]),
 ],
}

BODY["creation-site-internet-cannes"] = [
  ("Une clientèle qui change avec le calendrier", [
    "À Cannes, l'activité suit le calendrier des congrès et des festivals : Festival du film en mai, MIPIM au printemps, Cannes Lions en juin, Yachting Festival en septembre, sans compter les salons professionnels toute l'année. Pendant ces semaines, des milliers de visiteurs cherchent un restaurant, un chauffeur, un coiffeur ou un artisan, souvent depuis leur téléphone et souvent en anglais.",
    "Un site à jour, avec des horaires et des tarifs adaptés à ces périodes, vous fait profiter de ce flux au lieu de le laisser aux plateformes."]),
  ("Le Cannet, Mougins, Mandelieu, Cagnes-sur-Mer : vos clients sont autour", [
    "Le reste de l'année, ce sont surtout les habitants de l'agglomération qui vous font vivre. Ils cherchent « près de chez moi » ou tapent votre métier suivi de leur commune. Votre site indique clairement les communes où vous travaillez, de Cagnes-sur-Mer à Mandelieu-la-Napoule, pour ressortir sur ces recherches.",
    "Nous travaillons à distance, ce qui permet de garder des prix bas, mais nous sommes à Cannes si vous préférez en parler de vive voix."]),
  ("Déjà des sites en ligne sur la Côte d'Azur", [
    "Parmi nos réalisations, un chauffeur privé basé à Cannes qui couvre Nice, Monaco et Saint-Tropez, avec réservation en ligne et site en quatre langues. Vous pouvez lire son histoire, et celle de nos autres projets, sur la page <a href=\"/realisations/\">Réalisations</a>."]),
]

# 17/11/2026 (passage SEO) : titres alignés sur les requêtes vues dans la Search Console + une section chacun
SEO_TITLE = {
  "site-internet-concession-automobile": "Site web automobile pour concession et négociant VO",
  "site-internet-agence-immobiliere": "Site internet agence immobilière indépendante, en 48 h",
  "site-internet-services-a-domicile": "Site internet services à la personne et à domicile",
}
BODY["site-internet-concession-automobile"].append(("Négociant VO, mandataire, garage qui vend", [
  "Le modèle ne sert pas qu'aux concessions de marque. Un négociant en véhicules d'occasion, un mandataire auto ou un garage qui vend quelques voitures par mois a les mêmes besoins : montrer son stock proprement, répondre vite aux demandes et inspirer confiance à un acheteur qui ne le connaît pas encore.",
  "Le site s'adapte à votre taille : dix véhicules ou deux cents, la présentation reste claire, et chaque voiture garde sa page tant qu'elle est à vendre."]))
BODY["site-internet-agence-immobiliere"].append(("L'estimation en ligne, porte d'entrée des mandats", [
  "Un propriétaire qui pense vendre commence presque toujours par chercher la valeur de son bien. Le formulaire d'estimation du site lui demande l'adresse, le type de bien, la surface, le nombre de pièces et l'état, puis sa demande arrive dans votre espace « Mes clients ». Vous le rappelez avec une estimation argumentée, ou vous fixez une visite.",
  "C'est souvent le premier contact qui mène à un mandat, bien avant que le bien n'apparaisse sur les portails."]))
BODY["site-internet-services-a-domicile"].append(("Déclaration, agrément : ce que le site doit afficher", [
  "Pour que vos clients profitent du crédit d'impôt, votre entreprise doit être déclarée comme organisme de services à la personne, une démarche qui se fait en ligne sur le portail NOVA. Certaines activités demandent en plus un agrément ou une autorisation, notamment la garde d'enfants de moins de trois ans et l'aide aux personnes âgées ou handicapées.",
  "Le site affiche votre numéro de déclaration et, le cas échéant, votre agrément : c'est ce que les familles vérifient avant de vous confier leur domicile ou leurs proches."]))
FAQ_EXTRA["site-internet-services-a-domicile"] = FAQ_EXTRA.get("site-internet-services-a-domicile", []) + [
  ("Le site convient-il à une entreprise de services à la personne ?", "Oui : ménage, repassage, jardinage, garde d'enfants, aide aux seniors. Le site présente vos services, votre zone, le crédit d'impôt et votre numéro de déclaration.")]

# 17/11/2026 (2e passage SEO) : titres alignés sur les requêtes vues dans la Search Console
SEO_TITLE.update({
  "site-internet-infirmier-liberal": "Site internet infirmière ou infirmier libéral",
  "site-internet-traiteur": "Site web traiteur : menus, devis et réservations",
  "site-internet-kinesitherapeute": "Site internet kinésithérapeute : cabinet et rendez-vous",
})

# 23/11/2026 (Anthony : « améliore encore SEO ») : « site internet plombier » = requête n°1 de la Search Console (21 impressions/7 j, position 58).
# Sources : arrêté du 24 janvier 2017 modifié (Légifrance, INC, DGCCRF), loi n° 96-603 art. 22-2 (CAPEB).
BODY_EXTRA["site-internet-plombier-electricien"] = BODY_EXTRA.get("site-internet-plombier-electricien", []) + [
  ("Prix, devis, assurance : ce que la loi demande… et ce que le site affiche", [
    "Depuis le 1er avril 2017, un artisan qui fait du dépannage, de la réparation ou de l'entretien chez un particulier (plomberie, électricité, serrurerie, vitrerie, chauffage…) doit informer le client de ses prix avant d'intervenir : taux horaire ou forfaits, frais de déplacement, et caractère gratuit ou payant du devis. Ces informations doivent aussi figurer sur ses supports publicitaires, site internet compris.",
    "Le devis détaillé est devenu obligatoire dès le premier euro pour ces interventions à domicile : l'ancien seuil de 150 € a disparu. Seule l'urgence absolue, quand il faut faire cesser un danger pour les personnes ou pour les locaux, échappe à ces règles.",
    "Si votre activité est soumise à l'assurance décennale, vos devis et factures doivent indiquer l'assurance souscrite, les coordonnées de l'assureur et la zone géographique couverte.",
    "Le modèle a une rubrique « Tarifs » prévue pour ça : taux horaire, déplacement, forfaits courants (débouchage, remplacement d'un chauffe-eau, mise aux normes d'un tableau). Vous les tenez à jour vous-même, et l'espace client génère vos devis en PDF avec votre logo et vos mentions."]),
  ("Urgence ou rendez-vous : deux parcours sur la même page", [
    "Le client en panne veut appeler tout de suite : le bouton d'appel reste visible en bas de l'écran sur téléphone. Celui qui prévoit des travaux préfère décrire son besoin et être rappelé : le formulaire de demande de rappel lui sert à ça, et la demande arrive dans votre espace et par e-mail.",
    "Indiquez clairement vos horaires et si vous intervenez le soir et le week-end : c'est l'une des premières choses que vérifie un client avant d'appeler."]),
]
FAQ_EXTRA["site-internet-plombier-electricien"] = FAQ_EXTRA.get("site-internet-plombier-electricien", []) + [
  ("Dois-je afficher mes tarifs sur mon site de plombier ?", "Pour le dépannage, la réparation et l'entretien chez les particuliers, l'arrêté du 24 janvier 2017 vous impose d'informer le client de vos prix avant l'intervention, y compris sur vos supports publicitaires : taux horaire ou forfaits, frais de déplacement, devis gratuit ou payant. La rubrique Tarifs du site est faite pour ça."),
  ("Un devis est-il obligatoire pour un petit dépannage ?", "Oui : depuis le 1er avril 2017, le devis détaillé est obligatoire dès le premier euro pour les dépannages, réparations et entretiens à domicile, sauf urgence absolue. Votre espace MyCreativeSite génère ces devis en PDF."),
]

# 25/11/2026 (tâche de nuit) : toiletteur, toilettage seul ou avec pension (source : bpifrance-creation.fr, fiche « Garde de chiens et chats », mise à jour du 18/08/2025 ; code rural L214-6-1)
_add("site-internet-toiletteur", [
  ("Toilettage seul ou avec une pension : ce qui change", [
    "Le toilettage n'apparaît pas dans la liste des activités pour lesquelles le code rural exige une qualification avec les animaux de compagnie. La garde, elle, y figure. Si vous gardez des chiens ou des chats à la journée ou pour la nuit, ou si vous vendez des animaux, les règles ne sont plus les mêmes.",
    "Pour la garde, au moins une personne en contact direct avec les animaux doit justifier d'une certification professionnelle reconnue, d'une formation habilitée suivie d'une évaluation (au moins 17 heures pour une seule catégorie d'animaux), ou d'un certificat de capacité obtenu avant 2016. L'activité se déclare à la DDPP au moins 30 jours avant de commencer.",
    "Il faut aussi un contrat écrit en deux exemplaires pour chaque garde, avec l'identification de l'animal et les dates, et un registre des entrées et sorties. Si vous proposez ces services, le site les présente sur une page à part, avec ce que le client doit apporter (carnet de santé, numéro d'identification)."]),
  ("Les informations à donner avant le rendez-vous", [
    "Un client qui vient pour la première fois veut savoir combien de temps dure le toilettage, s'il peut rester, s'il doit revenir chercher son animal et comment il sera prévenu. Le site répond à ces questions sur la page des prestations, ce qui évite les appels et les retards.",
    "Indiquez aussi vos conditions : ce qui se passe en cas de retard ou d'annulation, si vous acceptez les chiens non vaccinés ou les chiennes en chaleur, et comment vous gérez un pelage très emmêlé. Annoncé à l'avance, un supplément ou une tonte courte ne surprend personne."]),
],[
  ("Faut-il un diplôme pour ouvrir un salon de toilettage ?", "Le toilettage seul n'est pas dans la liste des activités du code rural qui demandent une qualification avec les animaux. Si vous gardez aussi des animaux (pension, garde à la journée), une certification ou une formation habilitée devient obligatoire pour au moins une personne au contact des animaux."),
])
