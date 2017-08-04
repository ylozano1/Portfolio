curl -X POST --user "c76d64c8-7f44-460e-8935-0b3ef4c0abae":"5QGYg45FqujB" \
--header "Content-Type: text/plain;charset=utf-8" \
--data-binary "@{path_to_file}/profile.txt" \
"https://gateway.watsonplatform.net/personality-insights/api/v3/profile?version=2016-10-20"

{
  "word_count": 15223,
  "processed_language": "en",
  "personality": [
    {
      "trait_id": "big5_openness",
      "name": "Openness",
      "category": "personality",
      "percentile": 0.8011555009553,
      "raw_score": 0.77565404255038,
      "children": [
        . . .
      ]
    },
    {
      "trait_id": "big5_conscientiousness",
      "name": "Conscientiousness",
      "category": "personality",
      "percentile": 0.81001753184176,
      "raw_score": 0.66899984888815,
      "children": [
        . . .
      ]
    },
    {
      "trait_id": "big5_extraversion",
      "name": "Extraversion",
      "category": "personality",
      "percentile": 0.64980796071382,
      "raw_score": 0.56817738781166,
      "children": [
        . . .
      ]
    },
    {
      "trait_id": "big5_agreeableness",
      "name": "Agreeableness",
      "category": "personality",
      "percentile": 0.94786124793821,
      "raw_score": 0.80677815631809,
      "children": [
        . . .
      ]
    },
    {
      "trait_id": "big5_neuroticism",
      "name": "Emotional range",
      "category": "personality",
      "percentile": 0.5008224041628,
      "raw_score": 0.46748200007024,
      "children": [
        . . .
      ]
    }
  ],
  "needs": [
    {
      "trait_id": "need_challenge",
      "name": "Challenge",
      "category": "needs",
      "percentile": 0.67362332054511,
      "raw_score": 0.75196348037675
    },
    . . .
  ],
  "values": [
    {
      "trait_id": "value_conservation",
      "name": "Conservation",
      "category": "values",
      "percentile": 0.89268222856139,
      "raw_score": 0.72135308187423
    },
    . . .
  ],
  "behavior": [
    {
      "trait_id": "behavior_sunday",
      "name": "Sunday",
      "category": "behavior",
      "percentage": 0.21392532795156
    },
    . . .
    {
      "trait_id": "behavior_saturday",
      "name": "Saturday",
      "category": "behavior",
      "percentage": 0.077699293642785
    },
    {
      "trait_id": "behavior_0000",
      "name": "0:00 am",
      "category": "behavior",
      "percentage": 0.4561049445005
    },
    . . .
    {
      "trait_id": "behavior_2300",
      "name": "11:00 pm",
      "category": "behavior",
      "percentage": 0.12310797174571
    }
  ],
  "consumption_preferences": [
    {
      "consumption_preference_category_id": "consumption_preferences_shopping",
      "name": "Purchasing Preferences",
      "consumption_preferences": [
        {
          "consumption_preference_id": "consumption_preferences_automobile_ownership_cost",
          "name": "Likely to be sensitive to ownership cost when buying automobiles",
          "score": 0
        },
        . . .
      ]
    },
    {
      "consumption_preference_category_id": "consumption_preferences_health_and_activity",
      "name": "Health & Activity Preferences",
      "consumption_preferences": [
        {
          "consumption_preference_id": "consumption_preferences_eat_out",
          "name": "Likely to eat out frequently",
          "score": 1
        },
        . . .
      ]
    },
    {
      "consumption_preference_category_id": "consumption_preferences_environmental_concern",
      "name": "Environmental Concern Preferences",
      "consumption_preferences": [
        {
          "consumption_preference_id": "consumption_preferences_concerned_environment",
          "name": "Likely to be concerned about the environment",
          "score": 0
        }
      ]
    },
    {
      "consumption_preference_category_id": "consumption_preferences_entrepreneurship",
      "name": "Entrepreneurship Preferences",
      "consumption_preferences": [
        {
          "consumption_preference_id": "consumption_preferences_start_business",
          "name": "Likely to consider starting a business in next few years",
          "score": 1
        }
      ]
    },
    {
      "consumption_preference_category_id": "consumption_preferences_movie",
      "name": "Movie Preferences",
      "consumption_preferences": [
        {
          "consumption_preference_id": "consumption_preferences_movie_romance",
          "name": "Likely to like romance movies",
          "score": 1
        },
        . . .
      ]
    },
    {
      "consumption_preference_category_id": "consumption_preferences_music",
      "name": "Music Preferences",
      "consumption_preferences": [
        {
          "consumption_preference_id": "consumption_preferences_music_rap",
          "name": "Likely to like rap music",
          "score": 1
        },
        . . .
      ]
    },
    {
      "consumption_preference_category_id": "consumption_preferences_reading",
      "name": "Reading Preferences",
      "consumption_preferences": [
        {
          "consumption_preference_id": "consumption_preferences_read_frequency",
          "name": "Likely to read often",
          "score": 0
        },
        . . .
      ]
    },
    {
      "consumption_preference_category_id": "consumption_preferences_volunteering",
      "name": "Volunteering Preferences",
      "consumption_preferences": [
        {
          "consumption_preference_id": "consumption_preferences_volunteer",
          "name": "Likely to volunteer for social causes",
          "score": 0
        },
        . . .
      ]
    }
  ],
  "warnings": []
}
