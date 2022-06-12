export class Card {
    constructor(day, date=null, timeslots, parent, type='origin') {
        this.day = day;
        this.date = date;
        this.timeslots = new Map([['no_group',[]]]);
        this.type = type; //Origin or destination
        this.parent = parent;
        this.element = this.defineElement();
    }
    getElement(){
        return this.element;
    }
    getElementRectangle(){
        return this.element.querySelector('.rectangle');
    }
    getDay(){
        return this.day;
    }
    getDate(){
        return this.date;
    }
    getTimeslots(){
        return this.timeslots;
    }
    getTimeslotsAsElements(){
        return this.timeslots.map((timeslot, i) => {timeslot.element});
    }
    defineElement(){
        let unwrap = ({day, index}) => ({day, index});
        var element = document.createElement('div');
        element.classList.add('availability-card');
        element.setAttribute('id', this.day);
        element.innerHTML = `
            <div class="header2 color-shade-grey">${this.day}</div>
            <div class="body1 color-shade-grey">${this.date}</div>
            <div class="rectangle"></div>
        `;
        // console.log("Parent", this.parent);
        return element;
    }
    attachElementToParent(){
        this.parent.appendChild(this.element);
    }
    appendTimeslotToSelf(timeslot){
        const timeslots = this.timeslots;
        const type = this.type;
        const element = timeslot.element;
        if(type == 'origin'){
            console.log("ORIGN");
            timeslots.get('no_group').push(timeslot)
            element.classList.remove("selected");
            this.getElementRectangle().appendChild(element);
        }
        else if (type == 'destination'){
            console.log("DESTINATION");
            const day = this.day;
            if (!timeslots.has(day)){
                timeslots.set(day, []);
            }
            timeslots.get(day).push(timeslot);
            element.classList.add("selected");
            this.getElementRectangle().appendChild(element);
            
        }
    }
}

export class Timeslot {
    constructor(window, capacity, origin_card, destination_card) {
        this.window = window;
        this.capacity = capacity;
        this.parent = origin_card;
        this.origin_card = origin_card;
        this.origin_card_insertionpoint = origin_card.getElementRectangle();
        this.destination_card = destination_card;
        this.destination_card_insertionpoint = origin_card.getElementRectangle();
        this.element = this.defineElement();
    }
    attachEventHandler(){
        
        function timeslotClickHandler(parent, origin_card, destination_card){
            const element = this;
            
            console.log(element);
            // const origin_card_element = this.origin_card.getElementRectangle();
            // const destination_card_element = this.destination_card.getElementRectangle();
            if (parent == origin_card){
                console.log("Destination Card", destination_card)
                destination_card.querySelector(".rectangle").appendChild(element);
            }
            else if (parent == destination_card){
                console.log("Origin Card")
                origin_card.getElementRectangle().appendChild(this.element);
            }
        }

        const element = this.element;
        const parent = this.parent;
        const origin_card = this.origin_card;
        const destination_card = this.destination_card;
        $(document).ready(() => {
            $("#available-container").ready(function () {
                element.addEventListener('click', timeslotClickHandler(parent, origin_card, destination_card));
            });
        })        
    }
    
    
    getWindow(){
        return this.window;
    }
    getCapacity(){
        return this.capacity;
    }
    getElement(){
        return this.element;
    }
    getOriginObject(){
        return this.origin_card;
    }
    getDestinationObject(){
        return this.destination_card;
    }
    getOriginElement(){
        return this.origin_card.element.querySelector('.rectangle');
    }
    getDestinationElement(){
        return this.destination_card.element.querySelector('.rectangle');
    }
    moveToOrigin(){
        var element = this.getOriginElement;
        element.appendChild(this.element);
    }
    moveToDestination(){
        var element = this.getDestinationElement;
        element.appendChild(this.element);
    }
    defineElement(){
        const window = this.window;
        var element = document.createElement('div');
        element.classList.add('timeslot');
        element.innerHTML = `
            <div class="body2">${this.window[0]} - ${this.window[1]}</div>
        `;
        return element;
    }
    attachElementToOrigin(){
            this.origin_card.getElementRectangle().appendChild(this.element);
    }
}