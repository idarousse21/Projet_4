<h1 align ="center">Explication et lancement du code</h1>

------------------------------
<h2 align = "center"> Application et bibliothèques </h2>

<p>
    Pour employer le code, tout d'abord, installez l'application python.
<ul>
    <li>
        <a href = "https://www.python.org/downloads/">Python </a>
    </li>
</ul>
</p>
<p>
    Nous utiliserons également les bibliothèques python;
    <ul>
        <li>
            <a href = "https://tinydb.readthedocs.io/en/latest/">Tinydb</a>
        </li>
        <li>
            <a href = "https://flake8.pycqa.org/en/latest/">flake8-html</a>
        </li>
    </ul>
</p>


<h2 align = "center"> Lancement du code </h2>
<p>Pour commencer, vous devez lancer l'invite de commande et employer les commandes suivantes:
    <ol>
            <li>Clonez le projet:<br/>
                git clone https://github.com/idarousse21/Projet_4.git </li>
            <li>Dirigez-vous sur le dossier cloné:<br/>
                cd Projet_4 </li>
            <li>Créez un environnement virtuel:<br/>
                python -m venv env</li>
            <li>Puis activation de l'environnement virtuel:<br/>
                Sur Windows:<br/>
                env\Scripts\activate<br/>
                Sous Mac/Linus:<br/>
                source/env/Scripts/activate
            <li>Configurez la bibliothèque Tinydb:<br/>
                pip install -r Requirements.txt</li>
            <li>Lancez le logiciel:<br/>
                python main_view.py</li>
            <li>Pour générer un fichier flake8-html taper sur l'invite de commande:<br/>
                "flake8 --format = html --htmldir = flake-rapport" pour créer le rapport</li>
    </ol>
    