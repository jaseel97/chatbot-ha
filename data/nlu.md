## intent:greet
- hi 
- hello 
- hey 
- helloo 
- hellooo 
- g morining 
- gmorning 
- good morning 
- morning 
- good day 
- good afternoon 
- good evening 
- greetings 
- greeting 
- good to see you 
- its good seeing you 
- how are you 
- how're you 
- how are you doing 
- how ya doin' 
- how ya doin 
- how is everything 
- how is everything going 
- how's everything going 
- how is you 
- how's you 
- how are things 
- how're things 
- how is it going 
- how's it going 
- how's it goin' 
- how's it goin 
- how is life been treating you 
- how's life been treating you 
- how have you been 
- how've you been 
- what is up 
- what's up 
- what is cracking 
- what's cracking 
- what is good 
- what's good 
- what is happening 
- what's happening 
- what is new 
- what's new 
- what is new

## intent:goodbye
- see you around
- see you later
- ciao
- see ya
- see you
- tata
- ta ta
- good bye
- cyah
- cya
- byr
-goodbyr

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- exactly
- yeah
- yep

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- nope
- negative

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?
- who are you?

## intent:thank
- thanks
- thank you
- merci
- ty
- thnks
- thankyou
- thx

## intent:chitchat
- chitchat
- I feel bored
- Whats the weather like?
- Care for a drink
- Talk to me

## intent:search_property
- I want to [buy](property_action) [land](property_type)
- I want to [rent](property_action) [land](property_type)
- I want to [lease](property_action) [land](property_type)

- want to [buy](property_action) [land](property_type)
- want to [rent](property_action) [land](property_type)
- want to [lease](property_action) [land](property_type)

- need [land](property_type)

- I need [land](property_type)
- looking for [land](property_type)
- I'm looking for [land](property_type)
- Im looking for [land](property_type)
- I am looking for [land](property_type)
- [land](property_type)
- looking for [agricultural](property_class) [land](property_type)

- I want to [lease](property_action) some [commercial](property_class) [land](property_type)
- I want to [rent](property_action) some [commercial](property_class) [land](property_type)
- I want to [buy](property_action) some [commercial](property_class) [land](property_type)

- I'd like to [rent](property_action) some [industrial](property_class) [land](property_type)
- I'd like to [lease](property_action) some [industrial](property_class) [land](property_type)
- I'd like to [buy](property_action) some [industrial](property_class) [land](property_type)

-[commercial](property_class) [land](property_type)
-[industrial](property_class) [land](property_type)
-[residential](property_class) [land](property_type)
-[agricultural](property_class) [land](property_type)

-[commercial](property_class) 
-[industrial](property_class) 
-[residential](property_class)
-[agricultural](property_class)

-[rent](property_action)
-[buy](property_action)
-[lease](property_action)

-[house](property_type)
-[villa](property_type)
-[appartment](property_type)
-[land](property_type)
-[building](property_type)
-[shop](property_type)
-[office](property_type)

-[Ernakulam](district)
-[Palakkad](district)
-[Malappuram](district)
-[Kottayam](district)

-[Palluruthy](town)
-[Kazhakootam](town)
-[Veeranakavu](town)
-[Uzhamalackal](town)

- I'm looking for a [house](property_type)
- I'm looking for a [villa](property_type) to [rent](property_action)
- I'd like to see 3BHK [houses](property_type) in [Ernakulam](district)
- I want to see [villas](property_type) near [Aluva](town)

- I am looking for a [commercial](property_class) [office](property_type) for [rent](property_action) in [Kazhakootam](town), [Thiruvananthapuram](district)
- I want to [buy](property_action) [agricultural](property_class) [land](property_type) in [Mannarkkad](town) in [Palakkad](district) district

- Want to [rent](property_action) [house](property_type)
- Show [land](property_type) for [rent](property_action) in [Palluruthy](town)

## synonym:house
- home
- villa

## lookup:town
    data/towns.txt

## lookup:district
    data/districts.txt