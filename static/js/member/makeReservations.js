// METHOD 1 For getting dynamically added jquery dom elements

$(".body2").text("Wagwan");
console.log(jsonTimeslots);

function loadAvailabilities(jsonTimeslots) {
    {Object.keys(teamBios).map((teamKey) => {
        return (
            <>
                <TeamName key={teamKey}>
                    <b>{teamKey}</b>
                </TeamName>
                <Team>
                    {teamBios[teamKey].map((memberObject) => {
                        return (
                            <TeamMember
                                key={memberObject.name}
                                name={memberObject.name}
                                linkedin={memberObject.linkedin}
                                instagram={memberObject.instagram}
                                otherLink={memberObject.otherLink}
                                bio={memberObject.bio}
                                roles={memberObject.roles}
                                image={memberObject.image}
                            />
                        );
                    })}
                </Team>
            </>
        );
    })}


    // O.
};

loadAvailabilities(jsonTimeslots)
