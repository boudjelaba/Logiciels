const sideMenu = document.querySelector("aside");
const profileBtn = document.querySelector("#profile-btn");
const themeToggler = document.querySelector(".theme-toggler");
const nextDay = document.getElementById('nextDay');
const prevDay = document.getElementById('prevDay');

profileBtn.onclick = function() {
    sideMenu.classList.toggle('active');
}
window.onscroll = () => {
    sideMenu.classList.remove('active');
    if(window.scrollY > 0){document.querySelector('header').classList.add('active');}
    else{document.querySelector('header').classList.remove('active');}
}

themeToggler.onclick = function() {
    document.body.classList.toggle('dark-theme');
    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active')
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active')
}

let setData = (day) =>{
    document.querySelector('table tbody').innerHTML = ' '; //Pour effacer les données du tableau précédent ; 
    let daylist = ["Dimmache", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    document.querySelector('.timetable div h2').innerHTML = daylist[day];
    switch(day){
        case(1): day = Lundi; break;
        case(2): day = Mardi; break;
        case(3): day = Mercredi; break;
        case(4): day = Jeudi; break;
        case(5): day = Vendredi; break;
        case(6): day = Samedi; break;
        case(0): day = Dimanche; break;
    }

    day.forEach(sub => {
        const tr = document.createElement('tr');
        const trContent = `
                            <td>${sub.time}</td>
                            <td>${sub.roomNumber}</td>
                            <td>${sub.subject}</td>
                            <td>${sub.type}</td>
                        `
        tr.innerHTML = trContent;
        document.querySelector('table tbody').appendChild(tr)                        
    });
}

let now = new Date();
let today = now.getDay(); // Retournera le jour présent en valeur numérique ;
let day = today; // Pour empêcher la valeur actuelle de changer ;

function timeTableAll(){
    document.getElementById('timetable').classList.toggle('active');
    setData(today);
    document.querySelector('.timetable div h2').innerHTML = "Horaire journalier";
}
nextDay.onclick = function() {
    day<=5 ? day++ : day=0;  // Sinon une doublure
    setData(day);
}
prevDay.onclick = function() {
    day>=1 ? day-- : day=6;    
    setData(day);
}

setData(day); // Pour définir les données dans le tableau sur la fenêtre de chargement.
document.querySelector('.timetable div h2').innerHTML = "Horaire journalier"; // Pour éviter d'écraser l'en-tête lors du chargement ;
