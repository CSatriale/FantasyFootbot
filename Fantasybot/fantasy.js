"use strict";

// n is position
// r is round
// N is number of teams

const NumberOfTeams = 12;
const allDraftPicks = {};

for (let draftPosition = 1; draftPosition <= NumberOfTeams; draftPosition++) {
  const picks = [];

  for (let round = 1; round <= 16; round++) {
    let draftPick;

    if (round % 2 === 0) {
      draftPick = (round * NumberOfTeams) - draftPosition + 1;
    } else {
      draftPick = ((round - 1) * NumberOfTeams) + draftPosition;
    }

    picks.push(draftPick);
  }

  allDraftPicks[draftPosition] = picks;
}

console.log(JSON.stringify(allDraftPicks[1], null, 2));