// array describing the color for each team
// using camel case where the team names include a space


// array describing the drivers, sorted by position and with a rating describing the distance from the leading driver

/*const leaderboard = [
  {
    name: 'Lewis Hamilton',
    team: 'mercedes',
    rating: 'Leader'
  },
  {
    name: 'Lando Norris',
    team: 'mclaren',
    rating: 'DNF'
  },
  {
    name: 'Daniil Kvyat',
    team: 'toro rosso',
    rating: 'DNF'
  },
  {
    name: 'Nico Hulkenberg',
    team: 'renault',
    rating: 'DNF'
  }
];
*/

//var xhReq = new XMLHttpRequest();
//xhReq.open("GET", "all_team.json", false);
//xhReq.send(null);
function compare( a, b ) {
  if ( a.rating < b.rating ){
    return 1;
  }
  if ( a.rating > b.rating ){
    return -1;
  }
  return 0;
}

var leaderboard = [
    {
        "id": 1,
        "name": "Springhack",
        "participants": [
            {
                "id": 4,
                "firstName": "Styopa",
                "lastName": "Shch",
                "employeeRole": "DEVELOPER"
            },
            {
                "id": 5,
                "firstName": "Egor",
                "lastName": "Kon",
                "employeeRole": "TESTER"
            }
        ],
        "rating": 0.9
    },
    {
        "id": 2,
        "name": "Photolab",
        "participants": [],
        "rating": 1.1
    }
];

leaderboard = leaderboard.sort(compare);
//var leaderboard = JSON.parse(data);
console.log(leaderboard);

// target the table element in which to add one div for each driver
const main = d3
  .select('table');

// for each driver add one table row
// ! add a class to the row to differentiate the rows from the existing one
// otherwise the select method would target the existing one and include one row less than the required amount
const drivers = main
  .selectAll('tr.driver')
  .data(leaderboard)
  .enter()
  .append('tr')
  .attr('class', 'driver');

// in each row add the information specified by the dataset in td elements
// specify a class to style the elements differently with CSS

// position using the index of the data points
drivers
  .append('td')
  .text((d, i) => i + 1)
  .attr('class', 'position');


// name followed by the team
drivers
  .append('td')
  // include the last name in a separate element to style it differently
  // include the team also in another element for the same reason
  .html (({name}) => `${name.split(' ').map((part, index) => index > 0 ? `<strong>${part}</strong>` : `${part}`).join(' ')}`)
  // include a border with the color matching the team
  //.style.border-left=`4px solid red`;
  .attr('class', 'driver');

// rating from the first driver
drivers
  .append('td')
  .attr('class', 'rating')
  .append('span')
  .text(({rating}) => rating);