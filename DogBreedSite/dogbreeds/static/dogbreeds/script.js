

function dostuff() {

    localStorage.clear();

    var intelligenceRdbs = document.getElementsByName('intelligence');
    var sheddingRdbs = document.getElementsByName('shedding');
    var groomingRdbs = document.getElementsByName('grooming');
    var activityRdbs = document.getElementsByName('activity');
    var coatRdbs = document.getElementsByName('104');
    var droolsRdbs = document.getElementsByName('103');
    var goodWCRdbs = document.getElementsByName('102');
    var e = document.getElementById("sizePref");


    // do whatever you want with the checked radio
    var selectedIntelligence = getCheckedRdb(intelligenceRdbs).toLowerCase();
    var selectedShedding = getCheckedRdb(sheddingRdbs).toLowerCase();
    var selectedGrooming = getCheckedRdb(groomingRdbs).toLowerCase();
    var selectedActivity = getCheckedRdb(activityRdbs).toLowerCase();
    var selectedCoat = getCheckedRdb(coatRdbs).toLowerCase();
    var selectedDrools = getCheckedRdb(droolsRdbs).toLowerCase();
    var selectedGoodWC = getCheckedRdb(goodWCRdbs).toLowerCase();
    var sizePref = e.options[e.selectedIndex].value.toLowerCase();

    var dreamDog = {
        activity: selectedActivity,
        drools: selectedDrools,
        coat: selectedCoat,
        goodWithKids: selectedGoodWC,
        grooming: selectedGrooming,
        intelligence: selectedIntelligence,
        shedding: selectedShedding,
        size: sizePref,
    };

    // List all dogs with the dream dog features starting with size etc. then only loop through them

    var potentialDogBreeds = [];

    for( var i = 0; i < dogBreedData.length; i++) {

        var matchingFeatures = 0;

        if(dreamDog.activity == dogBreedData[i].activity.toLowerCase() || dreamDog.activity == "nopref") {
            matchingFeatures += 1;
        }

        if(dreamDog.drools == dogBreedData[i].drools.toLowerCase()) {
            matchingFeatures += 1;
        }

        if(dreamDog.coat == dogBreedData[i].coat.toLowerCase()) {
            matchingFeatures += 1;
        }

        if(dreamDog.goodWithKids == dogBreedData[i].goodWC.toLowerCase()) {
            matchingFeatures += 1;
        }

        if(dreamDog.grooming == dogBreedData[i].grooming.toLowerCase() || dreamDog.grooming == "nopref") {
            matchingFeatures += 1;
        }

        if(dreamDog.intelligence == dogBreedData[i].intelligence.toLowerCase() || dreamDog.intelligence == "nopref") {
            matchingFeatures += 1;
        }

        if(dreamDog.shedding == dogBreedData[i].shedding.toLowerCase() || dreamDog.shedding == "nopref") {
            matchingFeatures += 1;
        }

        console.log(dreamDog.size)

        if(dreamDog.size == dogBreedData[i].size.toLowerCase()) {
            matchingFeatures += 1;
        }

        if(matchingFeatures >= 5) {
            if (dreamDog.size == dogBreedData[i].size || dreamDog.goodWithKids == dogBreedData[i].goodWC) {
                potentialDogBreeds.push(dogBreedData[i]);
                localStorage.setItem('notExact', '1');
            }

            if (matchingFeatures >= 5) {
                potentialDogBreeds.push(dogBreedData[i]);
                localStorage.setItem('notExact', '2');
            }

        }
    }

    console.log("Potential dog breeds: \n" + potentialDogBreeds);

    localStorage.setItem('dogbreedName', potentialDogBreeds[0].name)
    localStorage.setItem('dogbreedImage', potentialDogBreeds[0].image)
    localStorage.setItem('dogbreedIntelligence', potentialDogBreeds[0].intelligence)
    localStorage.setItem('dogbreedActivity', potentialDogBreeds[0].activity)
    localStorage.setItem('dogbreedShedding', potentialDogBreeds[0].shedding)
    localStorage.setItem('dogbreedDrools', potentialDogBreeds[0].drools)
    localStorage.setItem('dogbreedGoodWC', potentialDogBreeds[0].goodWC)
    localStorage.setItem('dogbreedGrooming', potentialDogBreeds[0].grooming)
    localStorage.setItem('dogbreedCoat', potentialDogBreeds[0].coat)
    localStorage.setItem('dogbreedSize', potentialDogBreeds[0].size)
}


function getCheckedRdb(rdbs) {
    for (var i = 0; i < rdbs.length; i++) {
        if (rdbs[i].checked) {
            return rdbs[i].id;
        }
    }
}