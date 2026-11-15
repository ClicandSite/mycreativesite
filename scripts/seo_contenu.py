# -*- coding: utf-8 -*-
"""Contenus SEO enrichis, page par page (passes SEO automatiques, voir scripts/SEO_PLAN.md).
Chaque entrée remplace, pour la page du même slug dans build_seo.py : titre de l'onglet (seo_title),
meta description, H1, accroche, FAQ, et ajoute des sections de texte (body = [(H2, [paragraphes HTML])]).
Règles : uniquement les faits de scripts/BRIEF_CONTENU_SEO.md, prix identiques à ceux du site,
aucun texte recopié d'une page à l'autre, liens internes vers des pages qui existent."""

SEO = {

# ---------------------------------------------------------------- Pack Auto, Moto & Immo
"site-internet-diffusion-annonces-auto-immo": dict(
  seo_title="Site + diffusion d'annonces auto, moto et immo",
  meta="Site pro et diffusion d'annonces auto, moto ou immobilier en illimité sur Abracadeal, sans passerelle à payer. 99 €/mois, sans engagement.",
  h1="Site internet et diffusion d'annonces auto, moto et immobilier",
  lead="Garages qui vendent des véhicules, concessions auto et moto, agences immobilières : le Pack Auto, Moto & Immo réunit votre site professionnel et la diffusion illimitée de vos annonces sur Abracadeal. Vous saisissez un véhicule ou un bien une seule fois, le site, sa page Google et l'annonce suivent.",
  body=[
    ("Pourquoi réunir site et annonces dans un même outil ?", [
      "Quand un véhicule est vendu ou qu'un bien passe sous compromis, il faut d'habitude le retirer à plusieurs endroits : sur le site, sur les sites d'annonces, parfois dans un logiciel de diffusion payé à part. Chaque oubli fait sonner le téléphone pour rien et agace l'acheteur.",
      "Avec le Pack, votre stock vit dans votre espace client. Prix, photos, statut « vendu » : vous changez l'information à un seul endroit et votre site comme vos annonces Abracadeal sont synchronisés. Aucune passerelle ni logiciel de diffusion n'est à payer en plus.",
    ]),
    ("Ce que contient votre site", [
      "Votre site reprend le modèle de votre métier, au style que vous choisissez. Vos véhicules ou vos biens y sont présentés en vitrine, avec photos et fiches détaillées. Chaque annonce a sa propre page, avec un titre, un prix, des photos et une fiche technique, lisible par Google et facile à partager par message.",
      "Le Pack comprend tout ce que contient la formule Pro : espace client, devis en PDF, paiement en ligne (frais Stripe en plus), vos avis Google repris sur le site et les modifications faites par nous sur simple message. S'y ajoute le CRM : fichier clients, historique des demandes et relances, pour ne laisser filer aucun acheteur ni aucun vendeur.",
    ]),
    ("Deux versions, selon votre activité", [
      "<b>Concession auto et moto</b> : un site 100 % vente, avec le stock en vitrine, des fiches complètes, la reprise et le financement mis en avant. Pas d'atelier ni de prise de rendez-vous. Voyez le <a href=\"/site-internet-concession-automobile/\">modèle concession automobile</a> ou le <a href=\"/site-internet-concession-moto/\">modèle concession moto</a>.",
      "<b>Agence immobilière</b> : biens à vendre et à louer, DPE et GES affichés, demande d'estimation en ligne. Le <a href=\"/site-internet-agence-immobiliere/\">modèle agence immobilière</a> montre le rendu sur ordinateur et sur téléphone.",
      "Vous tenez un garage qui ne vend pas de véhicules et faites seulement l'entretien, les pneus ou les freins ? Le Pack n'est pas nécessaire : le <a href=\"/site-internet-garage/\">site pour garage</a> se fait dès la formule Essentiel.",
    ]),
    ("Comment ça marche", [
      "Vous choisissez la formule Pack Auto, Moto & Immo, votre métier, puis votre style parmi ceux proposés sur la page d'accueil. Vous envoyez vos informations et vos photos depuis votre téléphone, ou vous remplissez le site vous-même dans votre espace avec l'aperçu en direct.",
      "Votre SIRET est demandé au paiement : votre espace professionnel Abracadeal est alors ouvert et relié à votre site automatiquement, et votre page professionnelle Abracadeal est visible sur Google. Votre site est en ligne en 48 heures, et rien n'est facturé avant que vous l'ayez validé.",
    ]),
    ("Le prix du Pack", [
      "99 € par mois et 490 € de mise en ligne, une fois. Hébergement, nom de domaine à votre nom, version mobile et espace client sont inclus. TVA non applicable, art. 293 B du CGI : le prix affiché est le prix payé. Sans engagement : l'abonnement s'arrête à la fin du mois en cours. Le détail figure dans les <a href=\"/#tarifs\">tarifs</a> et les <a href=\"/cgv.html\">conditions générales</a>.",
    ]),
  ],
  faq=[
    ("Que remplace le Pack Auto, Moto & Immo ?", "Un site vitrine d'un côté, et une passerelle ou un logiciel de diffusion d'annonces de l'autre. Ici, les deux sont réunis dans un seul abonnement, sans coût par annonce."),
    ("Combien d'annonces puis-je publier ?", "Autant que vous voulez : les annonces sont illimitées sur Abracadeal et synchronisées avec votre site (prix, photos, vendus)."),
    ("Mes annonces sont-elles diffusées ailleurs que sur Abracadeal ?", "La diffusion se fait aujourd'hui sur Abracadeal. Votre site et la page Google de chaque véhicule ou de chaque bien restent par ailleurs visibles de tous."),
    ("Je fais seulement de l'entretien automobile, ai-je besoin du Pack ?", "Non. Un garage d'entretien (vidange, pneus, freins) peut choisir Essentiel, Pro ou Premium. Le Pack sert aux garages qui vendent des véhicules, aux concessions et aux agences immobilières."),
    ("Que se passe-t-il si j'arrête ?", "L'abonnement s'arrête à la fin du mois en cours et vos annonces sont retirées. Votre nom de domaine reste à vous, et on vous remet vos textes et vos photos."),
  ]),

# ---------------------------------------------------------------- Site pas cher
"site-internet-pas-cher": dict(
  seo_title="Site internet pas cher pour pros dès 29 €/mois",
  meta="Site internet pas cher pour artisans et commerçants : dès 29 €/mois + 190 € de mise en ligne, hébergement et domaine inclus, sans engagement.",
  h1="Création de site internet pas cher pour les professionnels",
  feats=[("Dès 29 € par mois","Hébergement, nom de domaine, version mobile, sécurité et espace client compris dans le prix."),
         ("190 € de mise en ligne, une fois","Personnalisation du modèle, textes rédigés, photos, installation : tout est compris."),
         ("Aucun engagement","Vous arrêtez quand vous voulez, l'abonnement s'arrête à la fin du mois en cours."),
         ("Pas de frais cachés","Le prix affiché est le prix payé (TVA non applicable). Les dépannages sont compris."),
         ("Le modèle de votre métier","Rubriques, textes et réservation déjà pensés pour votre activité : on l'adapte, on ne repart pas de zéro."),
         ("Moins de temps que le faire soi-même","Pas besoin d'apprendre un outil de création : on fait le site, vous le modifiez simplement.")],
  lead="Un site vitrine pas cher, mais un vrai site pensé pour votre métier : dès 29 € par mois et 190 € de mise en ligne, une seule fois. Hébergement, nom de domaine, version mobile et espace client sont compris, sans engagement de durée.",
  body=[
    ("Ce que vous payez, et rien d'autre", [
      "Un site internet se paie en deux temps chez MyCreativeSite : des frais de mise en ligne une seule fois, puis un abonnement mensuel. En Essentiel, c'est 190 € puis 29 € par mois. TVA non applicable, art. 293 B du CGI : le montant affiché est celui que vous réglez.",
      "Cet abonnement couvre ce qui, ailleurs, s'ajoute souvent sur la facture : l'hébergement sécurisé avec le cadenas HTTPS, le nom de domaine réservé à votre nom, la version mobile, les sauvegardes, les mises à jour, les pages de mentions légales et les dépannages à distance. Si vous n'avez pas de logo, on met votre nom en forme, offert.",
    ]),
    ("Pourquoi un site peu cher peut quand même être un bon site", [
      "Le prix bas ne vient pas d'un site au rabais : chaque métier a déjà son modèle, avec les rubriques, les textes et la réservation qui lui conviennent. Plutôt que de repartir de zéro, on adapte ce modèle à votre entreprise, à vos prix et à vos photos. C'est ce travail déjà fait qui permet le tarif.",
      "Le site est conçu d'abord pour le téléphone, là où la plupart de vos clients vous cherchent. Il présente clairement vos services, vos horaires et vos coordonnées, et l'agenda de réservation en ligne est inclus dès Essentiel : le client choisit un créneau libre, confirmé tout de suite.",
    ]),
    ("Trois formules, selon ce dont vous avez besoin", [
      "<b>Essentiel, 29 € par mois</b> (+ 190 € de mise en ligne) : pour être trouvé sur Google et recevoir des demandes. Devis en PDF à votre logo et QR code de votre site inclus.",
      "<b>Pro, 49 € par mois</b> (+ 290 €) : tout Essentiel, plus la réservation avec paiement en ligne (acompte ou totalité, frais Stripe en plus), vos avis Google affichés sur le site et les modifications faites par nous sur simple message.",
      "<b>Premium, 79 € par mois</b> (+ 490 €) : tout Pro, plus le CRM, le site en français et en anglais, le référencement local renforcé, la création de votre logo et de votre bannière et le style Signature. Pour vendre en ligne, la formule <a href=\"/site-internet-boutique-en-ligne/\">Boutique</a> est à 99 € par mois.",
    ]),
    ("Pas cher, et sans vous attacher", [
      "Aucun contrat sur 48 mois : vous restez parce que le site vous apporte des clients. Vous résiliez quand vous voulez et l'abonnement s'arrête à la fin du mois en cours. Votre nom de domaine est à votre nom : si vous partez, il vous est rendu gratuitement, avec vos textes et vos photos.",
      "Pour faire le point sur les budgets, notre guide <a href=\"/conseils/combien-coute-un-site-internet/\">combien coûte un site internet</a> détaille ce qu'il faut regarder avant de signer.",
    ]),
    ("Comment ça marche", [
      "Vous choisissez une formule, votre métier et votre style, puis vous envoyez votre nom, vos services, vos prix, vos horaires et quelques photos depuis votre téléphone. On rédige les textes et on installe tout. Vous voyez votre site sur une adresse provisoire, vous le validez, et il part en ligne. Rien n'est facturé avant votre validation. Ensuite, vous modifiez prix, horaires et photos vous-même : voyez notre page <a href=\"/site-internet-facile-a-modifier/\">site facile à modifier</a>.",
    ]),
  ],
  faq=[
    ("Combien coûte un site internet chez MyCreativeSite ?", "À partir de 29 € par mois et 190 € de mise en ligne, une fois, en formule Essentiel. Pro est à 49 € par mois (+ 290 €), Premium à 79 € par mois (+ 490 €)."),
    ("Qu'est-ce qui est compris dans l'abonnement ?", "L'hébergement sécurisé, le nom de domaine à votre nom, la version mobile, l'espace client, les sauvegardes, les mises à jour, les mentions légales et les dépannages à distance."),
    ("Y a-t-il des options payantes ?", "Elles sont facultatives : fiche Google optimisée (149 € une fois), logo et bannière (49 € une fois, offerts en Premium et Boutique), adresse mail pro (+ 5 € par mois) et site français / anglais (+ 10 € par mois, inclus en Premium et Boutique)."),
    ("Suis-je engagé sur une durée ?", "Non. Vous arrêtez quand vous voulez : l'abonnement s'arrête à la fin du mois en cours."),
    ("Quand est-ce que je paie ?", "Une fois votre site vu sur une adresse provisoire et validé. Rien n'est facturé avant."),
  ]),

# ---------------------------------------------------------------- Site clé en main
"site-internet-cle-en-main": dict(
  seo_title="Site internet clé en main pour artisans et TPE",
  meta="Site internet clé en main : nom de domaine, textes, hébergement, mentions légales et mise en ligne faits pour vous en 48 h. Dès 29 €/mois.",
  h1="Site internet clé en main : on s'occupe de tout pour vous",
  lead="Avec un site internet clé en main, vous n'avez rien de technique à faire : on réserve votre nom de domaine, on rédige vos textes, on installe et on héberge le site, et il est en ligne en 48 heures. Vous gardez ensuite la main sur vos prix, horaires et photos.",
  body=[
    ("Ce qui est fait pour vous", [
      "Le nom de domaine est réservé à votre nom, par exemple votre-entreprise.fr, et branché sur le site. Si vous en avez déjà un, on le récupère et vos clients gardent la même adresse. Le guide <a href=\"/aide/nom-de-domaine/\">relier votre nom de domaine</a> montre ce qu'il faut faire chez votre fournisseur.",
      "Les textes sont rédigés à partir des informations que vous nous donnez : vos services, vos prix, vos horaires, votre façon de travailler. Vous n'avez pas encore de logo ? Votre nom est mis en forme gratuitement. Les pages obligatoires, mentions légales et confidentialité, sont prêtes dès la mise en ligne.",
      "L'hébergement est rapide et sécurisé, avec le cadenas HTTPS. Sauvegardes, sécurité et mises à jour sont surveillées pour vous, et en cas de souci on répare à distance, sans frais.",
    ]),
    ("Ce que vous avez à faire", [
      "Choisir votre formule, votre métier et votre style : deux minutes. Puis remplir un formulaire simple depuis votre téléphone, avec votre nom, votre adresse, vos horaires, vos services, vos prix et vos photos : environ quinze minutes. Pas de rendez-vous, pas de visio : tout se fait en ligne et par mail, à votre rythme, même le soir.",
      "Vous préférez tout remplir vous-même ? C'est possible aussi : vous accédez tout de suite à votre espace, avec l'aperçu en direct de votre site.",
    ]),
    ("Un modèle déjà pensé pour votre métier", [
      "Clé en main ne veut pas dire générique. Chaque métier a son modèle : un <a href=\"/site-internet-restaurant/\">restaurant</a> affiche sa carte, un <a href=\"/site-internet-artisan-batiment/\">artisan du bâtiment</a> ses chantiers et sa demande de devis, un <a href=\"/site-internet-coiffeur-institut-beaute/\">salon de coiffure ou institut</a> sa prise de rendez-vous. Vous choisissez ensuite le style, couleurs et typographies, et vous pouvez en changer plus tard sans frais.",
      "Toutes les photos des modèles sont libres de droits : vous pouvez les garder ou les remplacer par les vôtres.",
    ]),
    ("Après la mise en ligne, vous restez autonome", [
      "Votre espace client vous permet de changer un prix, un horaire ou une photo depuis votre téléphone, en direct. En formules Pro et Premium, vous pouvez aussi nous envoyer vos changements par message et on s'en occupe.",
      "Vos réservations et demandes arrivent par mail et dans votre espace dès qu'un client réserve. L'agenda de réservation en ligne est inclus dès Essentiel.",
    ]),
    ("Le prix d'un site clé en main", [
      "Essentiel à 29 € par mois, Pro à 49 € par mois, Premium à 79 € par mois, avec des frais de mise en ligne une seule fois (190 €, 290 € ou 490 €). Sans engagement, et votre nom de domaine, vos textes et vos photos restent à vous si vous partez. Comparez les formules dans les <a href=\"/#tarifs\">tarifs</a>.",
    ]),
  ],
  faq=[
    ("Que veut dire « clé en main » chez MyCreativeSite ?", "Que vous n'avez rien de technique à faire : nom de domaine, textes, hébergement, sécurité, mentions légales et mise en ligne sont pris en charge."),
    ("Faut-il savoir se servir d'un ordinateur ?", "Pas besoin : quelques champs à remplir depuis votre téléphone suffisent, et toute la partie technique reste de notre côté."),
    ("Dois-je me déplacer ou prévoir une réunion ?", "Aucun déplacement ni appel vidéo : les échanges passent par le formulaire et par mail, quand ça vous arrange."),
    ("J'ai déjà un nom de domaine, je le garde ?", "Oui. On le récupère et on le branche sur votre nouveau site : vos clients gardent la même adresse."),
    ("Qui est propriétaire du site ?", "Vous. Le nom de domaine est enregistré à votre nom, et en cas de départ vos textes et vos photos vous sont remis."),
  ]),

# ---------------------------------------------------------------- Site rapide
"site-internet-rapide": dict(
  seo_title="Site internet rapide : en ligne en 48 heures",
  meta="Besoin d'un site internet rapidement ? Votre site pro en ligne en 48 h, sans rendez-vous, pensé pour le mobile. Dès 29 €/mois, sans engagement.",
  h1="Site internet rapide : votre site pro en ligne en 48 heures",
  lead="Ouverture, nouveau local, saison qui démarre : vous avez besoin d'un site maintenant. Une fois vos informations et vos photos reçues, votre site est en ligne en général sous 48 heures ouvrées, sans rendez-vous. Et c'est un site léger, pensé pour s'afficher vite sur téléphone.",
  body=[
    ("Pourquoi on peut aller aussi vite", [
      "Parce que le plus long est déjà fait. Chaque métier a un modèle conçu et testé, avec ses rubriques, sa réservation et ses textes de départ. Il ne reste qu'à y mettre votre nom, vos services, vos prix, vos horaires et vos photos.",
      "Et parce qu'il n'y a ni réunion ni allers-retours de maquettes. Tout passe par un formulaire simple, depuis votre téléphone. Vous pouvez aussi remplir le site vous-même dans votre espace client : vous y accédez tout de suite, avec l'aperçu en direct.",
    ]),
    ("Les étapes, du choix à la mise en ligne", [
      "<b>1. Vous choisissez</b> votre formule, votre métier et votre style : deux minutes. <b>2. Vous envoyez vos infos</b> : nom, adresse, horaires, services, prix et photos, environ quinze minutes. <b>3. On rédige les textes</b>, on installe tout et on branche votre nom de domaine.",
      "Vous voyez ensuite votre site sur une adresse provisoire, sur ordinateur et sur téléphone. Vous le validez et vous payez : votre nom de domaine est réservé et le site part en ligne. Rien n'est facturé avant votre validation.",
    ]),
    ("Rapide à faire, rapide à charger", [
      "Un site rapide, c'est aussi un site qui s'ouvre vite. Les pages sont légères, et le site est pensé d'abord pour le téléphone : c'est de là que la plupart de vos clients vous cherchent, souvent en 4G. La vitesse d'affichage sur mobile compte pour Google, et un visiteur qui attend trop longtemps repart.",
      "L'hébergement rapide et sécurisé, avec le cadenas HTTPS, est inclus dans toutes les formules, tout comme le nom de domaine et la version mobile.",
    ]),
    ("Rapide à modifier ensuite", [
      "Une fois en ligne, un prix, un horaire ou une photo se change en quelques secondes depuis votre espace client, et la modification est visible aussitôt. La page <a href=\"/site-internet-facile-a-modifier/\">site facile à modifier</a> montre comment, et vous pouvez essayer l'espace client sans inscription.",
    ]),
    ("Quel site pour aller vite ?", [
      "Les modèles existent déjà pour de nombreux métiers, par exemple <a href=\"/site-internet-plombier-electricien/\">plombier et électricien</a>, <a href=\"/site-internet-vtc/\">chauffeur VTC</a> ou <a href=\"/site-internet-boulangerie/\">boulangerie</a>. Côté prix : Essentiel à 29 € par mois (+ 190 € de mise en ligne), Pro à 49 € (+ 290 €), Premium à 79 € (+ 490 €), sans engagement. Pour un site sans rien à gérer, voyez aussi notre offre <a href=\"/site-internet-cle-en-main/\">site clé en main</a>.",
    ]),
  ],
  faq=[
    ("En combien de temps mon site est-il en ligne ?", "En général sous 48 heures ouvrées après réception de vos informations et de vos photos."),
    ("Que dois-je fournir ?", "Le nom de votre entreprise, votre adresse, vos services et prix, vos horaires, vos coordonnées et quelques photos. On rédige les textes à partir de ces informations."),
    ("Faut-il un rendez-vous ?", "Non. Pas de visio ni de réunion : un formulaire simple, depuis votre téléphone, suffit."),
    ("Est-ce que je vois le site avant de payer ?", "Oui. Vous le voyez sur une adresse provisoire, sur ordinateur et sur téléphone, et rien n'est facturé avant que vous l'ayez validé."),
    ("Un site rapide à charger, ça compte pour Google ?", "Oui : la vitesse sur mobile fait partie des critères pris en compte par Google, et un site lent fait partir les visiteurs."),
  ]),
}

# 12/11/2026 (Anthony : « fais une page SEO ») : page taxi enrichie
SEO["site-internet-taxi"] = dict(
  seo_title="Site internet pour taxi : réservation en ligne dès 29 €/mois",
  meta="Création de site internet pour taxi : réservation de course en ligne, transport conventionné CPAM, gares et aéroports, bouton d'appel. En ligne en 48 h, dès 29 €/mois, sans engagement.",
  h1="Création de site internet pour taxi : vos clients vous réservent en direct",
  lead="Habitués, patients, hôtels, voyageurs qui arrivent en gare ou à l'aéroport : avec votre propre site, ils vous trouvent sur Google et vous réservent sans passer par une centrale. Un site de taxi pensé pour le téléphone, en ligne en 48 h, dès 29 € par mois.",
  body=[
    ("Pourquoi un taxi a besoin de son propre site", [
      "Quand quelqu'un tape « taxi » suivi du nom de sa ville, Google affiche d'abord des résultats locaux : fiches d'entreprise, centrales de réservation, annuaires. Sans site, vous dépendez de ces intermédiaires pour être trouvé. Avec un site à votre nom, vous existez en direct, avec vos zones, vos services et votre numéro.",
      "Le site travaille surtout pour les courses réservées à l'avance : un départ tôt pour la gare, un transfert vers l'aéroport, des allers-retours réguliers pour des soins, une entreprise qui reçoit des visiteurs. Ce sont des clients fidèles, qui vous rappellent si vous avez été à l'heure. Votre site leur donne une façon simple de vous retrouver.",
      "Pour la prise en charge immédiate, le bouton d'appel et le bouton WhatsApp restent visibles en permanence sur téléphone : un geste suffit pour vous joindre."]),
    ("Le transport conventionné, un vrai argument", [
      "Si votre taxi est conventionné par l'Assurance maladie, dites-le clairement : beaucoup de patients et de familles cherchent un « taxi conventionné » pour une consultation, un examen, une séance de soins ou une hospitalisation, avec un bon de transport prescrit par le médecin.",
      "Le modèle met le transport conventionné en avant dans vos services, et vous y ajoutez les informations utiles depuis votre espace client : qui peut en bénéficier, les documents à préparer (prescription médicale de transport, carte Vitale), le tiers payant. Les demandes de course arrivent directement chez vous, avec le jour, l'heure et l'adresse."]),
    ("Des informations claires sur vos tarifs", [
      "Les tarifs des taxis sont réglementés : compteur, prise en charge, suppléments et, selon les villes, forfaits pour les aéroports ou les gares fixés par la préfecture. Votre site les présente simplement, pour rassurer avant la course : ce qui est au compteur, ce qui est au forfait, et les longues distances sur devis.",
      "Vous modifiez vous-même ces informations depuis votre espace client, par exemple quand un nouvel arrêté change les tarifs, sans rien connaître à l'informatique."]),
    ("Être trouvé dans votre ville et votre secteur", [
      "Pour qu'une personne qui cherche « taxi gare » ou « taxi aéroport » dans votre ville tombe sur vous, le site indique précisément votre commune de rattachement, les villes autour, les gares, aéroports, hôpitaux et cliniques que vous desservez. Ces mots, écrits naturellement, sont ce que Google lit pour vous proposer.",
      "Le site est rapide sur téléphone, sécurisé (HTTPS) et contient les données que Google sait lire (nom, téléphone, zone desservie). Pensez aussi à votre fiche Google Business Profile : le site et la fiche se renforcent l'un l'autre, et vos avis clients y comptent beaucoup."]),
    ("Ce que comprend votre site de taxi", [
      "<b>Réservation de course</b> dès l'accueil : départ, arrivée, date et heure. La demande arrive par mail et dans « Mes clients », et vous confirmez au client.",
      "<b>Votre véhicule et vos services</b> : nombre de places, bagages, siège enfant, accès pour personnes à mobilité réduite, paiement par carte à bord, langues parlées.",
      "<b>Vos mentions obligatoires</b> : nom de l'entreprise, numéro d'autorisation de stationnement et commune, conventionnement le cas échéant. Les mentions légales sont rédigées pour vous.",
      "<b>Version anglaise</b> pour la clientèle touristique et d'affaires (incluse en Premium), et <b>devis et bons en PDF</b> à votre nom depuis l'espace client.",
      "Vous êtes chauffeur VTC et pas taxi ? Voyez notre <a href=\"/site-internet-vtc/\">modèle de site pour chauffeur VTC</a>, pensé pour les réservations à l'avance et les forfaits."]),
  ],
  faq=[("Puis-je indiquer que je suis conventionné CPAM ?","Oui. Le transport de patients assis est mis en avant dans vos services, et vous ajoutez les documents à prévoir et la façon de réserver. Les demandes arrivent directement chez vous."),
       ("Je travaille avec une centrale de réservation, un site est-il utile ?","Oui : il vous apporte vos propres clients, ceux qui vous cherchent sur Google ou qui veulent rappeler le même chauffeur, sans commission sur la course."),
       ("Puis-je afficher mes tarifs et mes forfaits aéroport ?","Oui. Vous indiquez vos tarifs réglementés et vos forfaits, et vous les modifiez vous-même à tout moment depuis votre espace client."),
       ("Combien coûte un site de taxi ?","Dès 29 € par mois en Essentiel, plus 190 € de mise en ligne une seule fois. Hébergement, nom de domaine, version mobile et dépannages compris, sans engagement."),
       ("En combien de temps mon site est-il en ligne ?","En 48 h après réception de vos informations. Vous le voyez d'abord sur une adresse provisoire, sur ordinateur et téléphone.")])

# 12/11/2026 (Anthony : « les gens cherchent avant d'ouvrir l'entreprise ») : pages créateurs d'entreprise enrichies
SEO["site-internet-creation-entreprise"] = dict(
  seo_title="Site internet pour création d'entreprise dès 29 €/mois",
  body=[
    ("Pourquoi prévoir son site avant d'ouvrir", [
      "Quand on crée son entreprise, on pense au statut, à la banque, à l'assurance, au local. Le site internet passe souvent après, alors que c'est lui qui fait venir les premiers clients : avant d'appeler un professionnel qu'il ne connaît pas, presque tout le monde le cherche sur Google.",
      "Un site prêt le jour de l'ouverture vous fait gagner des semaines. Google a besoin de temps pour découvrir et classer un nouveau site : plus il est en ligne tôt, plus vite il remonte quand on cherche votre métier dans votre ville.",
      "C'est aussi une question de crédibilité : un site à votre nom, avec vos services, vos tarifs et vos coordonnées, rassure bien plus qu'une simple page sur un réseau social."]),
    ("Ce qu'il faut sur le site d'une nouvelle entreprise", [
      "<b>Ce que vous faites et où</b> : vos services, votre ville et votre secteur, écrits simplement. C'est ce que lisent les clients et Google.",
      "<b>Un moyen de vous joindre en un geste</b> : bouton d'appel sur téléphone, formulaire de contact, WhatsApp si vous l'utilisez.",
      "<b>Vos tarifs ou une fourchette de prix</b> : c'est l'information la plus recherchée, et elle évite les appels pour rien.",
      "<b>Des photos réelles</b> : votre local, vos réalisations, votre véhicule ou votre équipe, même peu nombreuses au début.",
      "<b>Les mentions légales</b> : nom de l'entreprise, forme juridique, SIREN, adresse, hébergeur. Elles sont obligatoires dès que le site est en ligne."]),
    ("Un budget adapté au démarrage", [
      "Au lancement, chaque euro compte. Plutôt qu'un devis d'agence à plusieurs milliers d'euros, MyCreativeSite fonctionne en abonnement : dès 29 € par mois, plus 190 € de mise en ligne une seule fois, sans engagement. Hébergement, nom de domaine, version mobile et dépannages sont compris.",
      "Votre site est fait à partir d'un modèle déjà conçu pour votre métier, en ligne en 48 h, et vous le modifiez vous-même depuis votre téléphone quand votre activité évolue. Pour aller plus loin, lisez notre <a href=\"/conseils/creer-son-entreprise-checklist/\">checklist de la création d'entreprise</a>."]),
  ]
)
SEO["site-internet-auto-entrepreneur"] = dict(
  seo_title="Site internet pour auto-entrepreneur dès 29 €/mois",
  body=[
    ("Un site pro sans plomber vos débuts", [
      "En micro-entreprise, les charges sont calculées sur votre chiffre d'affaires et le budget de départ est souvent serré. Un site à 29 € par mois, sans engagement, vous donne une vraie présence en ligne sans investissement lourd.",
      "Le site est fait à partir d'un modèle conçu pour votre métier, mis en ligne en 48 h, avec votre nom de domaine. Vous le modifiez seul, depuis votre téléphone : textes, photos, tarifs, horaires."]),
    ("Les mentions obligatoires d'un micro-entrepreneur", [
      "Un micro-entrepreneur n'est pas obligé d'avoir un site. Mais s'il en a un, celui-ci doit afficher des mentions légales : votre nom et prénom précédés ou suivis de la mention « EI » (entrepreneur individuel), votre numéro SIREN, l'adresse de l'entreprise, un moyen de vous contacter et les coordonnées de l'hébergeur du site.",
      "Si vous vendez en ligne ou prenez des réservations, des informations supplémentaires s'ajoutent (prix, conditions de vente, droit de rétractation selon les cas). Notre guide sur les <a href=\"/conseils/mentions-legales-site-professionnel/\">mentions légales d'un site professionnel</a> fait le point."]),
    ("Pour quels métiers ?", [
      "Coiffure ou esthétique à domicile, coach sportif, photographe, artisan du bâtiment, plombier ou électricien, chauffeur VTC, services à domicile, cours particuliers, consultant : chaque activité a son modèle, avec les rubriques qui comptent pour elle (réservation, devis, galerie, zone d'intervention).",
      "Et si votre activité grandit au-delà de la micro-entreprise, le site vous suit : vous changez de formule ou de statut sans tout refaire. Pour savoir si un site vaut le coup pour vous, lisez <a href=\"/conseils/auto-entrepreneur-site-internet/\">auto-entrepreneur : faut-il un site internet ?</a>"]),
  ]
)

# ---------------------------------------------------------------- Passe SEO du 15/11/2026
SEO["site-internet-facile-a-modifier"] = dict(
  seo_title="Site internet facile à modifier soi-même, dès 29 €/mois",
  meta="Site internet facile à modifier soi-même : prix, horaires, photos changés depuis votre téléphone, avec l'aperçu en direct. Dès 29 €/mois, sans engagement.",
  h1="Un site internet facile à modifier soi-même, depuis votre téléphone",
  lead="Changer un prix, annoncer une fermeture ou remplacer une photo ne devrait pas demander un appel à un prestataire. Avec MyCreativeSite, votre site est fait pour vous, puis vous le modifiez vous-même dans votre espace client, en voyant le résultat en direct avant d'enregistrer.",
  body=[
    ("Pourquoi c'est important de pouvoir modifier son site seul", [
      "Un site qui affiche des horaires d'hiver en plein été ou un tarif de l'an dernier fait perdre des clients sans qu'on s'en rende compte. Le visiteur se déplace pour rien, appelle pour vérifier, ou part chez un concurrent dont la page est à jour.",
      "Quand chaque changement passe par un prestataire, on le reporte. Quand il se fait en quelques secondes depuis son téléphone, on le fait tout de suite, entre deux clients. C'est la différence entre un site qui vit et une page oubliée."]),
    ("Ce que vous changez vous-même, sans compétence technique", [
      "<b>Vos prix et votre carte</b> : vous ajoutez, supprimez ou modifiez une ligne de tarif. <b>Vos horaires</b> : fermeture exceptionnelle, congés, horaires d'été. <b>Vos photos</b> : vous en prenez une avec votre téléphone et vous la mettez à la place de l'ancienne, elle est redimensionnée automatiquement.",
      "<b>Vos textes</b> : présentation, services, informations pratiques. <b>Votre style</b> : vous pouvez passer à un autre des 25 styles plus tard, sans frais et sans perdre vos textes. Ce sont des cases à remplir, comme un formulaire : la mise en page reste protégée, et un bouton annule la dernière modification si vous vous trompez."]),
    ("L'aperçu en direct : vous voyez avant de publier", [
      "Dans l'espace client, votre site s'affiche à côté de ce que vous tapez. Vous voyez la phrase changer, la photo se placer, le prix apparaître, sur ordinateur comme sur téléphone. Pas de surprise une fois en ligne.",
      "Vous pouvez essayer tout de suite, sans inscription, avec la <a href=\"/espace/?demo=restaurant\">démo de l'espace client</a> : c'est le même outil que celui que reçoivent nos clients."]),
    ("Vous préférez qu'on s'en occupe ? C'est prévu aussi", [
      "Pouvoir modifier seul ne veut pas dire devoir tout faire seul. Au départ, on rédige vos textes et on installe le site pour vous. Ensuite, en formules Pro (49 € par mois) et Premium (79 € par mois), vous nous envoyez un simple message avec le changement voulu, et on le fait.",
      "En Essentiel (29 € par mois + 190 € de mise en ligne), vous gardez la main sur vos prix, horaires et photos depuis l'espace client, et les dépannages à distance restent compris. Le détail est dans les <a href=\"/#tarifs\">tarifs</a>."]),
    ("Comment ça marche", [
      "Vous choisissez une formule, votre métier parmi les modèles, puis votre style. Vous envoyez vos informations et vos photos, ou vous remplissez le site vous-même avec l'aperçu en direct. Votre site est en ligne en général sous 48 heures ouvrées, sur une adresse provisoire d'abord : rien n'est facturé avant votre validation.",
      "Une fois en ligne, l'espace client vous montre aussi vos statistiques de visites, sans compter vos propres passages. Pour voir les modèles par métier, passez par la page <a href=\"/site-internet-cle-en-main/\">site internet clé en main</a> ou par notre offre <a href=\"/site-internet-rapide/\">site en ligne en 48 h</a>."]),
  ],
  faq=[
    ("Faut-il savoir coder pour modifier mon site ?", "Non. Vous remplissez des champs comme dans un formulaire, et l'aperçu vous montre le résultat avant d'enregistrer."),
    ("Puis-je modifier mon site depuis mon téléphone ?", "Oui. L'espace client fonctionne sur téléphone : vous changez un prix, un horaire ou une photo en quelques secondes."),
    ("Est-ce que je risque de casser la mise en page ?", "Non. La mise en page est protégée et vous pouvez annuler votre dernière modification en un clic."),
    ("Puis-je changer le style de mon site plus tard ?", "Oui, sans frais. Vos textes et vos photos sont conservés quand vous passez à un autre style."),
    ("Et si je n'ai pas le temps de m'en occuper ?", "En formules Pro et Premium, vous nous envoyez vos changements par message et on s'en occupe pour vous."),
  ])

SEO["site-internet-boutique-en-ligne"] = dict(
  seo_title="Création de boutique en ligne pas chère pour commerçants",
  meta="Création de boutique en ligne pas chère : catalogue, panier, paiement par carte, retrait ou livraison. 99 €/mois + 490 € de mise en ligne, sans commission.",
  h1="Création de boutique en ligne pas chère, à votre nom",
  lead="Créateurs, épiceries fines, caves, fleuristes, concept stores : la formule Boutique vous donne une vraie boutique en ligne à votre nom, avec catalogue, panier, paiement par carte, retrait ou livraison. 99 € par mois et 490 € de mise en ligne, sans engagement et sans commission de notre part sur vos ventes.",
  body=[
    ("Pourquoi vendre sur votre propre boutique", [
      "Les places de marché apportent du passage, mais prélèvent une part de chaque vente et gardent la relation avec le client. Sur votre boutique, l'acheteur commande chez vous, sous votre nom de domaine, et revient chez vous la fois suivante.",
      "Pour un commerce de quartier, c'est aussi un moyen de vendre en dehors des heures d'ouverture : le client voit vos produits le soir sur son téléphone, paie, puis passe les chercher ou se fait livrer."]),
    ("Ce que contient votre boutique en ligne", [
      "<b>Un catalogue clair</b>, avec photos, prix, rayons et filtres par budget, pensé d'abord pour le téléphone. <b>Un panier et le paiement par carte</b> : le paiement passe par votre propre compte Stripe et arrive sur votre compte bancaire, les frais de Stripe s'ajoutant à chaque paiement.",
      "<b>Retrait ou livraison</b> : retrait gratuit en boutique, ou livraison avec vos frais et votre seuil de livraison offerte. <b>Les commandes rangées</b> : chaque commande arrive dans votre espace, onglet Mes clients, avec son statut de paiement. Et vos produits sont publiés en illimité sur Abracadeal, synchronisés avec votre catalogue."]),
    ("Pourquoi elle reste peu chère", [
      "Une boutique sur mesure en agence se chiffre souvent en milliers d'euros, sans compter la maintenance. Ici, la boutique part d'un modèle déjà construit : on l'adapte à vos produits, à vos couleurs et à vos conditions de livraison au lieu de tout développer.",
      "L'abonnement comprend l'hébergement sécurisé, le nom de domaine à votre nom, la version mobile, les mises à jour, les sauvegardes et la maintenance à distance. La formule Boutique reprend aussi tout ce que contient Premium : CRM, site en français et en anglais, référencement local renforcé, logo et bannière offerts et style Signature."]),
    ("Votre catalogue, tenu depuis votre téléphone", [
      "Un nouveau produit arrive ? Vous prenez la photo, vous saisissez le nom et le prix dans votre espace client, et il est en ligne. Un article épuisé, une promotion, un changement de prix : la modification prend quelques secondes, avec l'aperçu en direct.",
      "La formule est pensée pour les petites boutiques, avec jusqu'à 40 produits mis en avant. Pour un très grand catalogue, mieux vaut nous en parler avant de commander. Pour préparer votre projet, lisez notre guide <a href=\"/conseils/creer-boutique-en-ligne-les-indispensables/\">créer une boutique en ligne : les indispensables</a>."]),
    ("Comment ça marche", [
      "Vous choisissez la formule Boutique, puis votre style. Vous envoyez vos informations, vos premières photos de produits et vos conditions de retrait ou de livraison. On installe la boutique, vous la voyez sur une adresse provisoire, et elle part en ligne en général sous 48 heures ouvrées. Rien n'est facturé avant votre validation.",
      "Vous préférez commencer par un site vitrine sans vente en ligne ? Les formules dès 29 € par mois sont détaillées sur la page <a href=\"/site-internet-pas-cher/\">site internet pas cher</a>. Pour commander, rendez-vous sur le <a href=\"/#commande\">formulaire de commande</a>."]),
  ],
  faq=[
    ("Combien coûte la boutique en ligne ?", "99 € par mois et 490 € de mise en ligne, une fois, sans engagement. TVA non applicable : le prix affiché est le prix payé. Les frais bancaires de Stripe s'ajoutent à chaque paiement."),
    ("Prenez-vous une commission sur mes ventes ?", "Non. Le paiement passe par votre propre compte Stripe et arrive sur votre compte bancaire. MyCreativeSite ne touche pas à vos ventes."),
    ("Combien de produits puis-je mettre en ligne ?", "La formule est pensée pour les petites boutiques, jusqu'à 40 produits mis en avant. Pour un très grand catalogue, parlons-en avant."),
    ("Mes clients peuvent-ils retirer leur commande en magasin ?", "Oui. Vous proposez le retrait gratuit en boutique, la livraison avec vos frais, ou les deux."),
    ("Mes produits apparaissent-ils ailleurs que sur ma boutique ?", "Oui : avec la formule Boutique, vos produits sont publiés en illimité sur Abracadeal, synchronisés avec votre catalogue."),
  ])

SEO["site-internet-plombier-electricien"] = dict(
  seo_title="Création site internet plombier, électricien, dépannage",
  meta="Création de site internet pour plombier et électricien : demande de rappel, zone d'intervention, tarifs, bouton d'appel. En ligne en 48 h, dès 29 €/mois.",
  h1="Création de site internet pour plombier et électricien",
  lead="Une fuite, un disjoncteur qui saute, plus d'eau chaude : le client cherche un artisan sur son téléphone, tout de suite. Votre site de plombier ou d'électricien lui montre vos services, votre zone et vos tarifs, et lui permet de vous appeler ou de demander un rappel en un geste.",
  feats=[("Demande de rappel","Problème, code postal, délai souhaité : la demande vous arrive par mail et dans votre espace « Mes clients »."),
         ("Interventions récentes","Le problème, la solution, le temps passé et le prix : la preuve concrète de votre travail."),
         ("Tarifs transparents","Déplacement, débouchage, recherche de fuite, remise en service : vos prix, fixés par vous."),
         ("Zone d'intervention","Vos communes et vos délais, pour être trouvé quand on cherche votre métier près de chez soi."),
         ("Bouton d'appel","Toujours visible sur téléphone, pour vous joindre en un geste en cas d'urgence."),
         ("Vos engagements","Assurances, garantie de la main-d'œuvre, prix annoncé avant de commencer : ce que vous proposez réellement.")],
  body=[
    ("Pourquoi un site aide un plombier ou un électricien", [
      "En dépannage, le client ne compare pas pendant des jours : il choisit vite, souvent parmi les premiers artisans qui lui inspirent confiance. Un site clair, avec un numéro qui s'appelle d'un seul doigt, des prix lisibles et des communes nommées, rassure au moment où il hésite.",
      "Le site travaille aussi pour les chantiers moins urgents : remplacement de chauffe-eau, mise aux normes du tableau, rénovation d'une salle de bain. Là, le client prend le temps de regarder vos interventions et vos engagements avant de demander un devis."]),
    ("Ce que contient votre site de dépannage", [
      "Le modèle dépannage est construit pour la plomberie, l'électricité et le chauffage, et convient aussi aux serruriers et vitriers. En haut de page, un formulaire court : le problème, le code postal, le délai souhaité. Juste en dessous, vos services, vos tarifs et votre zone d'intervention.",
      "La rubrique « Interventions récentes » montre des cas réels : le problème, ce que vous avez fait, le temps passé et le prix. Vous l'alimentez depuis votre téléphone, avec une photo, à la fin du chantier. Une rubrique « Nos engagements » présente ce que vous proposez vraiment : assurances, garantie, prix annoncé avant de commencer, moyens de paiement."]),
    ("Être trouvé dans votre secteur", [
      "Un artisan travaille sur un territoire. Votre site nomme vos communes et vos services, ce qui aide Google à comprendre où et pour quoi vous proposer. La formule Premium ajoute un référencement local renforcé, et la fiche Google optimisée est proposée en option à 149 €, une fois.",
      "Aucun site ne peut promettre une place précise dans Google, mais un site rapide, adapté au téléphone et précis sur votre zone part avec de bons atouts. Notre guide <a href=\"/conseils/etre-visible-sur-google-artisan-commercant/\">être visible sur Google quand on est artisan</a> donne les bonnes pratiques."]),
    ("Quelle formule pour un artisan du dépannage ?", [
      "<b>Essentiel, 29 € par mois</b> (+ 190 € de mise en ligne) : le site, les demandes de rappel, l'agenda de réservation, les devis en PDF à votre logo et le QR code de votre site, à coller sur le camion ou les factures.",
      "<b>Pro, 49 € par mois</b> (+ 290 €) : en plus, vos avis Google affichés sur le site, le bouton « Laisser un avis » et les modifications faites par nous sur simple message. <b>Premium, 79 € par mois</b> (+ 490 €) : CRM, site français et anglais, référencement local renforcé, logo et bannière offerts."]),
    ("Comment ça marche", [
      "Vous choisissez la formule, le métier « Plomberie, électricité, dépannage », puis votre style. Vous envoyez vos services, vos tarifs, vos communes et quelques photos depuis le chantier. On rédige les textes, on installe tout, et le site est en ligne en général sous 48 heures ouvrées après réception de vos informations. Vous changez ensuite vos prix et vos interventions vous-même.",
      "Vous travaillez surtout en rénovation ? Le <a href=\"/site-internet-artisan-batiment/\">site pour artisan du bâtiment</a> met en avant vos réalisations et vos devis. Vous démarrez votre activité ? Lisez <a href=\"/conseils/site-internet-plombier-electricien-les-indispensables/\">site de plombier ou d'électricien : les indispensables</a>."]),
  ],
  faq=[
    ("Combien coûte un site internet de plombier ou d'électricien ?", "Dès 29 € par mois et 190 € de mise en ligne avec la formule Essentiel, sans engagement. Hébergement, nom de domaine, version mobile et dépannages du site sont compris."),
    ("Comment je reçois les demandes de rappel ?", "Par mail et dans votre espace client, onglet Mes clients, avec le problème, le code postal et le délai souhaité."),
    ("Puis-je ajouter une intervention depuis le chantier ?", "Oui, depuis votre téléphone, avec la photo, la description et le prix."),
    ("Le site indique-t-il mes communes d'intervention ?", "Oui. Vous listez vos communes et vos délais, et vous pouvez les modifier quand votre secteur change."),
    ("Le site convient-il à un auto-entrepreneur ?", "Oui. La formule Essentiel est faite pour démarrer, et vous pouvez passer à une autre formule plus tard."),
    ("Je suis serrurier ou vitrier, le modèle me convient-il ?", "Oui. Le modèle dépannage s'adapte : vous remplacez les services et les tarifs par les vôtres."),
  ])

SEO["site-internet-garage"] = dict(
  seo_title="Site internet garage automobile : atelier et occasions",
  meta="Site internet pour garage automobile : rendez-vous atelier, forfaits, véhicules d'occasion avec une page Google chacun, annonces sur Abracadeal. 99 €/mois.",
  h1="Site internet pour garage automobile qui vend aussi des occasions",
  lead="Votre garage entretient des véhicules et en vend aussi ? Ce site réunit les deux : rendez-vous atelier et forfaits d'un côté, stock de voitures et de motos d'occasion de l'autre. Avec le Pack Auto, Moto & Immo, chaque véhicule a sa page sur Google et part en annonce sur Abracadeal.",
  feats=[("Prise de rendez-vous","Prestation, date souhaitée, immatriculation : la demande arrive par mail et dans votre espace « Mes clients »."),
         ("Forfaits et tarifs","Vidange, pneus, freins, climatisation : des prix affichés qui donnent confiance avant même l'appel."),
         ("Stock de véhicules","Voitures et motos avec photos, fiche technique complète, prix et statut (en vente, réservé, vendu), filtrables par marque, énergie et budget."),
         ("Une page Google par véhicule","Chaque occasion a sa propre page, avec titre, prix, photos et fiche technique, lisible par Google et partageable sur WhatsApp."),
         ("Annonces illimitées sur Abracadeal","Vos véhicules sont publiés et mis à jour automatiquement sur Abracadeal, sans passerelle à payer."),
         ("Demande de reprise","Le client envoie son immatriculation et son kilométrage pour une demande de reprise : un contact de plus à chaque visite.")],
  body=[
    ("Pourquoi un site pour un garage qui vend des véhicules", [
      "Un garage mixte a deux types de clients : l'automobiliste qui cherche où faire sa vidange ou ses pneus, et l'acheteur qui cherche une occasion près de chez lui. Les deux commencent par une recherche sur leur téléphone, et les deux veulent voir un prix avant d'appeler.",
      "Un seul site peut répondre aux deux : l'atelier remplit l'agenda, et le stock en ligne fait venir des acheteurs qui ont déjà repéré leur véhicule. Les rendez-vous et les demandes de reprise arrivent au même endroit, dans votre espace."]),
    ("Le côté atelier : rendez-vous et forfaits", [
      "Vos prestations sont présentées avec leurs prix : vidange, pneus, freins, climatisation, distribution, diagnostic. Le client choisit sa prestation, une date et indique son immatriculation ; la demande vous arrive par mail et dans l'onglet Mes clients.",
      "Vous indiquez aussi vos services pratiques : prêt de véhicule, dépose matinale, marques prises en charge. Horaires, jours de fermeture et tarifs se changent depuis votre téléphone, sans attendre personne."]),
    ("Le côté vente : votre stock d'occasions sur Google et sur Abracadeal", [
      "Dans l'onglet Mes véhicules, vous remplissez une vraie fiche : marque, modèle, année, kilométrage, énergie, boîte, puissance, équipements et jusqu'à 30 photos. Le véhicule apparaît dans la vitrine du site, filtrable par marque, énergie et budget, avec sa propre page lisible par Google.",
      "Le même véhicule est publié sur Abracadeal, synchronisé : si vous baissez le prix ou le passez en « vendu », le site et l'annonce suivent. Aucune passerelle ni logiciel de diffusion n'est à payer en plus. Le fonctionnement complet est détaillé sur la page du <a href=\"/site-internet-diffusion-annonces-auto-immo/\">Pack Auto, Moto &amp; Immo</a>."]),
    ("Quelle formule choisir pour votre garage ?", [
      "Vous vendez des véhicules : le Pack Auto, Moto &amp; Immo, à 99 € par mois et 490 € de mise en ligne. Il comprend tout Pro (paiement en ligne, avis Google sur le site, modifications faites par nous sur simple message), le CRM, les annonces illimitées sur Abracadeal et votre page professionnelle Abracadeal. Le SIRET est demandé au paiement.",
      "Vous faites seulement l'entretien et la réparation ? Le Pack n'est pas utile : votre site de garage d'entretien, avec la prise de rendez-vous atelier et vos forfaits, se fait dès la formule Essentiel, à 29 € par mois. Vous ne faites que de la vente, sans atelier ? Voyez le <a href=\"/site-internet-concession-automobile/\">site de concession automobile</a> ou la <a href=\"/site-internet-concession-moto/\">concession moto</a>."]),
    ("Comment ça marche", [
      "Vous choisissez la formule, le métier « Garage », puis votre style. Vous envoyez vos prestations, vos tarifs, vos horaires et vos premiers véhicules, ou vous les saisissez vous-même avec l'aperçu en direct. Le site est en ligne en général sous 48 heures ouvrées après réception de vos informations, et rien n'est facturé avant votre validation. Pour la liste des rubriques utiles, lisez <a href=\"/conseils/site-internet-garage-les-indispensables/\">site de garage : les indispensables</a>."]),
  ],
  faq=[
    ("Quelle formule pour un garage qui vend aussi des véhicules ?", "Le Pack Auto, Moto & Immo, à 99 € par mois et 490 € de mise en ligne, sans engagement. Un garage qui fait seulement l'entretien peut choisir Essentiel, Pro ou Premium, dès 29 € par mois."),
    ("Je peux ajouter mes véhicules moi-même ?", "Oui. Dans l'onglet Mes véhicules, vous remplissez une fiche complète avec jusqu'à 30 photos. Le site et Abracadeal se mettent à jour tout seuls."),
    ("Les motos sont-elles prises en charge ?", "Oui. La fiche accepte voitures, motos et scooters."),
    ("Comment je reçois les rendez-vous atelier ?", "Par mail et dans votre espace client, onglet Mes clients, avec la prestation, la date souhaitée et l'immatriculation."),
    ("Que devient une annonce quand le véhicule est vendu ?", "Vous le passez en « vendu » une seule fois : le site et l'annonce Abracadeal sont mis à jour ensemble."),
    ("Combien de temps pour être en ligne ?", "En général 48 heures ouvrées après réception de vos informations et photos."),
  ])
