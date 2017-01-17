/**
* @function addClass
* @param  {element} element      Element whose class name needs to be altered
* @param  {String } newClassName Class Name
* @return None
*/
const addClass = (element, newClassName) => {
    if (element !== undefined && newClassName !== undefined) {
        let classNames = element.className;
        if (!classNames.includes(newClassName)) {
            element.className += ` ${newClassName}`;
        }
    }
    return;
};

/**
* @function removeClass
* @param  {element} element      Element whose class name needs to be altered
* @param  {String } delClassName Class Name
* @return None
*/
const removeClass = (element, delClassName) => {
    if (element !== undefined && delClassName !== undefined) {
        if (element.className.includes(delClassName)) {
            element.className = element
                .className
                .replace(new RegExp('(?:^|\\s)' + delClassName + '(?:\\s|$)'), '');
        }
    }
    return;
};

/**
* @function getRandomInt
* @param  {int} min {Minimum value, inclusive}
* @param  {int} max {Maximum value, exclusive}
* @return {int} {Random number between range}
*/
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
};

/**
* @function toggle
* @param  {element} element {DOM element that needs to be toggled}
* @param  {display: type} type    {type of the element to be changed}
* @return
*/
const toggle = (element, type) => {
    const display = type || 'flex';
    if (element.style.display !== 'none' && element !== undefined) 
        element.style.display = 'none';
    else 
        element.style.display = display;
};