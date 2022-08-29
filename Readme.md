<h1 align ="center">Explication et lancement du code</h1>

------------------------------
<h2 align = "center"> Application </h2>

<p>
    Pour employer le code, tout d'abord, installez l'application python.
<ul>
    <li>
        <a href = "https://www.python.org/downloads/">Python </a>
    </li>
</ul>
</p>


<h2 align = "center"> Lancement du code </h2>
<p>Pour commencer, vous devez lancer l'invite de commande et employer les commandes suivantes:
    <ol>
            <li>Clonez le projet:<br/>
                git clone </li>
            <li>Dirigez-vous sur le dossier cloné:<br/>
                cd Projet </li>
            <li>Créez un environnement virtuel:<br/>
                python -m venv env</li>
            <li>Puis activation de l'environnement virtuel:<br/>
                Sur Windows:<br/>
                env\Scripts\activate<br/>
                Sous Mac/Linus:<br/>
                source/env/Scripts/activate
            <li>Lancez le logiciel:<br/>
                python main_view.py</li>
            <li>Pour générer un fichier flake8-html taper sur l'invite de commande:<br/>
                "pip install flake8-html" pour installer le plug-in<br/>
                Et "flake8 --format = html --htmldir = flake-rapport" pour créer le rapport</li>
    </ol>
    