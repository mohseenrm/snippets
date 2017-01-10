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