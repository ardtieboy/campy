'use strict';

const e = React.createElement;

function move(position) {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", '/tripod/' + position, false ); // false for synchronous request
        xmlHttp.send( null );
        console.log(xmlHttp.responseText);
      }

class ArrowButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { direction : props.direction}
  }

  render() {
    return e(
      'button',
      { onClick: () => move(this.state.direction) },
        e('span',
            {className: "glyphicon glyphicon-arrow-"+this.state.direction})
    );
  }
}

const upDomContainer = document.querySelector('#up_button');
ReactDOM.render(e(ArrowButton, {direction: "up"}), upDomContainer);
const downDomContainer = document.querySelector('#down_button');
ReactDOM.render(e(ArrowButton, {direction: "down"}), downDomContainer);
const leftDomContainer = document.querySelector('#left_button');
ReactDOM.render(e(ArrowButton, {direction: "left"}), leftDomContainer);
const rightDomContainer = document.querySelector('#right_button');
ReactDOM.render(e(ArrowButton, {direction: "right"}), rightDomContainer);