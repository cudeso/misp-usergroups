# misp-usergroups

During the [MISP Summit 0x05](https://2019.hack.lu/misp-summit/) a presentation from [RichieB2B](https://github.com/RichieB2B) mentioned [@nederMISP](https://twitter.com/nedermisp). This inspired me to start a similar group for Belgium [@belgoMISP](https://twitter.com/belgomisp). And someone started a group for the US [@us4misp](https://twitter.com/us4misp).

This repository was then build to *list the MISP user groups worldwide*. In the good old MISP tradition, all is stored in JSON. 

Send a PR if you want your group added.

| Name | Description | Country | Twitter |
|------|-------------|---------|---------|
| belgoMISP | Belgian MISP Users | be | @belgoMISP |
| nederMISP | De Nederlandse MISP-gebruikersgroep | nl | @nederMISP |
| us4misp | MISP USA Users and Friends | us | @us4misp |
| francomisp | French speaking MISP instance dedicated to OSINT | fr | @francomisp |
| ItaliaMisp | Italian speaking MISP instance dedicated to OSINT | it | @ItaliaMisp |
| SwedishMISP | The Swedish MISP community | se | @SwedishMISP |
| NorwegianMISP | The Norwegian MISP community | no | @NorwegianMISP |
| DanishMISP | The Danish MISP User Group | dk | @danishmisp |
| auMISP | Australian MISP User Group | au | @auMISP |

# Meetings

Some suggestions for user group meetings
* Discuss usage of MISP outside of traditional threat intelligence cases
* Custom taxonomies and tagging
* Internal MISP modules
* Air-gapped MISP systems
* ...

# Todo
* Autogenerate a world map based on country code

# Schema

Format of MISP user groups

# JSON 

~~~~json
{
        "name": "Shortname of user group (required)",
        "meta-category": "Type of the group, currently only public is used (required)",
        "description": "Description of the group (required)",
        "contact":
        {
                "twitter": "Twitter handle of the group (optional)",
                "website": "Website of the group (optional)",
                "chat": "Chat channel (optional)",
                "affiliation": "Organizational affiliation (optional)"
        },
        "geometry":
        {
                "country": "country code ISO 3166-1 alpha-2 code (required)"
        },
        "services":
        {
                "feed": "Public feed (optional)",
                "misp": "MISP instance  (optional)"
        },
        "community": "Link to https://www.misp-project.org/communities/#known-existing-and-public-misp-communities (optional)"
}
~~~~
