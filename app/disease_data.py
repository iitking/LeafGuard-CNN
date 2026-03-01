"""
LeafGuard AI - Plant Disease Knowledge Base
Contains botanical descriptions, symptoms, causes, organic treatments,
and chemical treatments for all 38 trained PlantVillage classes.
"""

from typing import Dict, Any

DISEASE_KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    "Apple___Apple_scab": {
        "plant": "Apple",
        "disease": "Apple Scab",
        "is_healthy": False,
        "severity": "Moderate to High",
        "pathogen": "Venturia inaequalis (Fungus)",
        "summary": "Fungal infection causing velvety olive-green to black lesions on leaves and fruit, causing premature leaf drop and deformed fruit.",
        "symptoms": [
            "Olive-green, velvety spots on leaf surface.",
            "Yellowing around leaf spots leading to early defoliation.",
            "Cracked, corky brown lesions on fruit surface."
        ],
        "organic_remedies": [
            "Apply neem oil or sulfur-based organic fungicides at early bud break.",
            "Spray baking soda solution (1 tbsp baking soda + 1 tsp horticultural oil per gallon water).",
            "Collect and destroy fallen infected leaves to interrupt the fungal life cycle."
        ],
        "chemical_remedies": [
            "Apply Myclobutanil, Captan, or Mancozeb sprays during spring wet periods.",
            "Rotate fungicide chemical classes to prevent resistance build-up."
        ],
        "prevention": [
            "Plant resistant apple varieties (e.g., Liberty, Freedom, Enterprise).",
            "Prune branches annually to increase airflow and sunlight penetration.",
            "Avoid overhead irrigation; water at base of tree."
        ]
    },
    "Apple___Black_rot": {
        "plant": "Apple",
        "disease": "Black Rot",
        "is_healthy": False,
        "severity": "High",
        "pathogen": "Botryosphaeria obtusa (Fungus)",
        "summary": "Causes leaf frog-eye spots, limb cankers, and firm black rot in ripening fruit.",
        "symptoms": [
            "Small purple specks expanding into brown circular spots with purple margins (frog-eye leaf spot).",
            "Fruit rots into dark brown/black shriveled mummies.",
            "Sunken reddish-brown cankers on branches."
        ],
        "organic_remedies": [
            "Prune out dead wood, fire-blight strikes, and mummified fruits in winter.",
            "Apply copper sulfate or liquid copper spray before spring growth resumes.",
            "Keep trees vigorous with balanced organic compost."
        ],
        "chemical_remedies": [
            "Spray Captan or Thiophanate-methyl from pink blossom stage through harvest."
        ],
        "prevention": [
            "Prune wounded branches at least 6-8 inches below cankered areas.",
            "Ensure proper orchard sanitation and destroy infected trimmings."
        ]
    },
    "Apple___Cedar_apple_rust": {
        "plant": "Apple",
        "disease": "Cedar Apple Rust",
        "is_healthy": False,
        "severity": "Moderate",
        "pathogen": "Gymnosporangium juniperi-virginianae (Fungus)",
        "summary": "Complex two-host rust fungus cycling between Eastern red cedar/junipers and apple trees.",
        "symptoms": [
            "Bright orange-yellow circular spots on upper leaf surfaces.",
            "Small tubular spore cups (aecia) on undersides of leaves.",
            "Premature defoliation and fruit drop in heavy infections."
        ],
        "organic_remedies": [
            "Apply sulfur or copper octanoate spray early in spring when cedar galls swell.",
            "Remove nearby wild red cedar trees within a 1-mile radius if practical."
        ],
        "chemical_remedies": [
            "Spray Myclobutanil (Immunox) or Propiconazole when apple buds show pink."
        ],
        "prevention": [
            "Select rust-immune apple cultivars (e.g., Redfree, Priscilla, Enterprise).",
            "Inspect surrounding junipers and prune out cedar-apple galls in winter."
        ]
    },
    "Apple___healthy": {
        "plant": "Apple",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "The apple foliage is vibrant, robust, and free from visible pathogenic infections.",
        "symptoms": ["Smooth, green leaves without spots, necrosis, or deformities."],
        "organic_remedies": ["Maintain balanced organic feeding with compost tea and mulch."],
        "chemical_remedies": ["No chemical treatment required."],
        "prevention": ["Maintain routine monitoring, proper drip irrigation, and annual pruning."]
    },
    "Blueberry___healthy": {
        "plant": "Blueberry",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Foliage exhibits vigorous growth and dark green leaves with optimal vigor.",
        "symptoms": ["Crisp, green leaves without chlorosis or necrotic leaf spots."],
        "organic_remedies": ["Maintain acidic soil pH (4.5 to 5.5) using pine bark mulch and sulfur."],
        "chemical_remedies": ["No chemical treatment required."],
        "prevention": ["Ensure acidic soil, regular watering, and good root aeration."]
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "plant": "Cherry",
        "disease": "Powdery Mildew",
        "is_healthy": False,
        "severity": "Moderate",
        "pathogen": "Podosphaera clandestina (Fungus)",
        "summary": "White powdery fungal growth covering leaves and young shoots, stunting shoot growth.",
        "symptoms": [
            "White or grayish powdery patches on upper and lower leaf surfaces.",
            "Leaves curl upwards, become brittle, and drop prematurely.",
            "Distorted shoots and scarred young cherry fruit."
        ],
        "organic_remedies": [
            "Spray potassium bicarbonate (3 tbsp per gallon water) or neem oil.",
            "Apply milk spray dilution (40% milk, 60% water) under direct sunlight."
        ],
        "chemical_remedies": [
            "Apply Myclobutanil, Triflumizole, or sulfur at petal fall."
        ],
        "prevention": [
            "Avoid excessive nitrogen fertilization which promotes tender succulent growth.",
            "Prune canopy regularly to increase light penetration and air movement."
        ]
    },
    "Cherry_(including_sour)___healthy": {
        "plant": "Cherry",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Leaves and shoots are healthy, glossy, and unblemished.",
        "symptoms": ["Lush green leaves with strong vigor and no discoloration."],
        "organic_remedies": ["Apply balanced organic fertilizer during early spring."],
        "chemical_remedies": ["No chemical intervention needed."],
        "prevention": ["Prune dormant branches in winter and monitor during wet spring cycles."]
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "plant": "Corn (Maize)",
        "disease": "Gray Leaf Spot (Cercospora)",
        "is_healthy": False,
        "severity": "High",
        "pathogen": "Cercospora zeae-maydis (Fungus)",
        "summary": "One of the most destructive corn leaf diseases worldwide, causing severe reduction in photosynthesis.",
        "symptoms": [
            "Tan to gray rectangular lesions bounded strictly by leaf veins.",
            "Lesions coalesce, blighting entire leaves prematurely.",
            "Stalk lodging and reduced grain fill."
        ],
        "organic_remedies": [
            "Practice minimum 2-year crop rotation with non-host crops (soybean, sorghum).",
            "Incorporate crop residues deep into soil to speed decomposition of fungal spores."
        ],
        "chemical_remedies": [
            "Apply strobilurin or triazole fungicides (e.g., Pyraclostrobin, Azoxystrobin) at VT/R1 growth stages."
        ],
        "prevention": [
            "Plant gray leaf spot resistant hybrid seed corn.",
            "Adopt reduced plant density to increase canopy airflow in high-humidity areas."
        ]
    },
    "Corn_(maize)___Common_rust_": {
        "plant": "Corn (Maize)",
        "disease": "Common Rust",
        "is_healthy": False,
        "severity": "Moderate",
        "pathogen": "Puccinia sorghi (Fungus)",
        "summary": "Airborne fungal pathogen forming cinnamon-brown powdery pustules across leaves.",
        "symptoms": [
            "Oval to elongate cinnamon-brown pustules scattered across both leaf surfaces.",
            "Pustules rupture epidermal tissue, releasing rust-colored powdery spores.",
            "Leaves turn chlorotic and desiccate under heavy spore loads."
        ],
        "organic_remedies": [
            "Plant early in the season to avoid peak windborne spore migration.",
            "Ensure balanced fertilization without surplus nitrogen."
        ],
        "chemical_remedies": [
            "Apply Pyraclostrobin, Tebuconazole, or Mancozeb if rust appears before tasseling on susceptible lines."
        ],
        "prevention": [
            "Select resistant hybrids with Rp genes.",
            "Scout weekly during cool, moist weather (60-77°F / 16-25°C)."
        ]
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "plant": "Corn (Maize)",
        "disease": "Northern Corn Leaf Blight",
        "is_healthy": False,
        "severity": "High",
        "pathogen": "Exserohilum turcicum (Fungus)",
        "summary": "Forms large cigar-shaped lesions on leaves, causing widespread leaf death and yield losses.",
        "symptoms": [
            "Long, elliptical, grayish-green to tan lesions (cigar-shaped, 1-6 inches long).",
            "Dark olive-colored spores forming inside lesions during humid conditions.",
            "Extensive leaf necrosis starting on lower leaves moving upwards."
        ],
        "organic_remedies": [
            "Rotate fields with non-grass crops for at least 1-2 seasons.",
            "Plow under corn stubble post-harvest to reduce fungal overwintering."
        ],
        "chemical_remedies": [
            "Apply Azoxystrobin + Difenoconazole or Pyraclostrobin when lesions appear on ear leaf."
        ],
        "prevention": [
            "Plant certified disease-resistant corn varieties (with Ht resistance genes).",
            "Maintain optimal soil drainage and avoid pooling irrigation."
        ]
    },
    "Corn_(maize)___healthy": {
        "plant": "Corn (Maize)",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Corn plant shows thick green blades with active photosynthesis and normal stalk development.",
        "symptoms": ["Uniform green leaves with clear venation and no discoloration or pustules."],
        "organic_remedies": ["Apply organic matter and balanced side-dress nitrogen fertilizer."],
        "chemical_remedies": ["None required."],
        "prevention": ["Maintain weed control and balanced soil fertility."]
    },
    "Grape___Black_rot": {
        "plant": "Grape",
        "disease": "Black Rot",
        "is_healthy": False,
        "severity": "High",
        "pathogen": "Guignardia bidwellii (Fungus)",
        "summary": "Damaging fungal disease causing circular leaf spots and converting grape berries into hard black mummies.",
        "symptoms": [
            "Small reddish-brown circular spots on leaves with dark borders and tiny black dots inside.",
            "Berries develop soft brown rot spots, then shrivel into wrinkled, hard black mummies.",
            "Black elliptical lesions on canes and shoots."
        ],
        "organic_remedies": [
            "Prune away and burn all mummified fruit clusters during winter dormancy.",
            "Apply copper-based organic fungicides before rain events starting at bud break."
        ],
        "chemical_remedies": [
            "Apply Mancozeb, Captan, or Myclobutanil at early bloom, pre-bloom, and post-bloom."
        ],
        "prevention": [
            "Train vines for open canopy architecture to maximize air circulation and sunlight.",
            "Keep vineyard floor mowed and free from fallen leaf litter."
        ]
    },
    "Grape___Esca_(Black_Measles)": {
        "plant": "Grape",
        "disease": "Esca (Black Measles)",
        "is_healthy": False,
        "severity": "High to Critical",
        "pathogen": "Phaeomoniella chlamydospora & Fomitiporia mediterranea (Fungi)",
        "summary": "Complex wood rot and vascular fungal disease causing tiger-stripe foliar patterns and berry spotting.",
        "symptoms": [
            "'Tiger stripe' appearance on leaves with yellow/red chlorosis between veins and necrotic margins.",
            "Small dark purple spots ('measles') on the skin of white or red berries.",
            "Sudden vine wilting (apoplexy) during hot, dry summer weather."
        ],
        "organic_remedies": [
            "Seal pruning wounds immediately with pruning paste containing Trichoderma biocontrol agents.",
            "Prune vines during late winter dry periods to avoid wound infection."
        ],
        "chemical_remedies": [
            "Apply paint wound sealants containing Thiophanate-methyl right after pruning cuts."
        ],
        "prevention": [
            "Remove and burn dead or heavily infected vine cordons.",
            "Disinfect pruning shears regularly with 70% alcohol between cuts."
        ]
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "plant": "Grape",
        "disease": "Leaf Blight (Isariopsis)",
        "is_healthy": False,
        "severity": "Moderate",
        "pathogen": "Pseudocercospora cladosporioides (Fungus)",
        "summary": "Foliar blight forming irregular necrotic lesions on older leaves, reducing photosynthetic capacity.",
        "symptoms": [
            "Irregular brown or black necrotic lesions with subtle yellow halos on leaf blades.",
            "Premature defoliation of lower leaves late in the season.",
            "Reduced sugar accumulation and delayed fruit ripening."
        ],
        "organic_remedies": [
            "Apply sulfur or copper formulations after harvest and during wet spells.",
            "Ensure good leaf removal around grape clusters."
        ],
        "chemical_remedies": [
            "Apply Mancozeb or Strobilurin fungicides at first sign of foliar spotting."
        ],
        "prevention": [
            "Maintain canopy trimming to decrease humidity within the foliage zone.",
            "Remove leaf debris from the vineyard floor."
        ]
    },
    "Grape___healthy": {
        "plant": "Grape",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Grapevine canopy is green, expansive, and free of leaf lesions or cane cankers.",
        "symptoms": ["Lush green leaves, clean canes, and well-developed berry clusters."],
        "organic_remedies": ["Apply balanced organic compost and maintain mulch."],
        "chemical_remedies": ["None needed."],
        "prevention": ["Prune cleanly in winter and keep proper shoot positioning."]
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "plant": "Orange / Citrus",
        "disease": "Citrus Greening (Huanglongbing - HLB)",
        "is_healthy": False,
        "severity": "Critical",
        "pathogen": "Candidatus Liberibacter asiaticus (Bacteria, spread by Asian Citrus Psyllid)",
        "summary": "Devastating bacterial disease with no cure, causing mottled leaves, bitter lopsided green fruit, and tree death.",
        "symptoms": [
            "Asymmetrical yellow blotchy mottle on leaves (blotches cross leaf veins unevenly).",
            "Yellow veins and twig dieback.",
            "Small, lopsided, bitter fruit that stays green at the bottom; premature fruit drop."
        ],
        "organic_remedies": [
            "Release biological control agents (Tamarixia radiata wasp) to suppress psyllid populations.",
            "Spray horticultural oil or insecticidal soap to control citrus psyllid nymphs.",
            "Provide foliar micronutrient sprays (zinc, manganese, iron) to support tree vigor."
        ],
        "chemical_remedies": [
            "Control Asian citrus psyllid vectors with Imidacloprid, Thiamethoxam, or Cypermethrin.",
            "Severely infected trees must be removed and destroyed to protect nearby groves."
        ],
        "prevention": [
            "Use certified disease-free nursery stock.",
            "Scout constantly for psyllid vectors and yellow leaf mottling.",
            "Quarantine citrus plants and prohibit moving uncertified saplings."
        ]
    },
    "Peach___Bacterial_spot": {
        "plant": "Peach",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "severity": "Moderate to High",
        "pathogen": "Xanthomonas arboricola pv. pruni (Bacteria)",
        "summary": "Bacterial infection causing shot-hole leaves, twig cankers, and pitting on peach skin.",
        "symptoms": [
            "Angular, water-soaked leaf spots turning purple-brown, drying out and dropping out ('shot-hole' effect).",
            "Severe early leaf drop exposing fruit to sunscald.",
            "Sunken, gummy cracked spots on peach fruit."
        ],
        "organic_remedies": [
            "Apply dormant copper sprays in late fall and early spring before bud break.",
            "Use Bacillus subtilis-based bio-bactericides during growing season."
        ],
        "chemical_remedies": [
            "Spray Oxytetracycline (Mycoshield) or copper bactericides at low rates to avoid phytotoxicity."
        ],
        "prevention": [
            "Plant resistant peach varieties (e.g., Clayton, Candor, Harrow Beauty).",
            "Avoid planting on light, sandy soils without windbreaks (blowing sand exacerbates leaf cuts)."
        ]
    },
    "Peach___healthy": {
        "plant": "Peach",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Foliage is vibrant green, pliable, and show no signs of spotting or bacterial cankers.",
        "symptoms": ["Elongated deep-green leaves with clear margins and vigorous shoot extension."],
        "organic_remedies": ["Apply balanced organic fertilizer during spring."],
        "chemical_remedies": ["None required."],
        "prevention": ["Prune open center in late winter and maintain regular moisture."]
    },
    "Pepper,_bell___Bacterial_spot": {
        "plant": "Bell Pepper",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "severity": "High",
        "pathogen": "Xanthomonas euvesicatoria (Bacteria)",
        "summary": "Damaging seedborne bacterial disease causing leaf drop, sunscald on fruits, and necrotic spots.",
        "symptoms": [
            "Small water-soaked circular lesions turning brown with yellow halos.",
            "Severe leaf drop leaving fruit exposed to direct sunburn.",
            "Raised, wart-like brown scabs on bell pepper skin."
        ],
        "organic_remedies": [
            "Spray copper hydroxide combined with Bacillus subtilis.",
            "Practice drip irrigation rather than overhead sprinklers to prevent splash dispersal."
        ],
        "chemical_remedies": [
            "Apply copper bactericide mixed with Mancozeb to boost efficacy."
        ],
        "prevention": [
            "Purchase certified disease-free seeds or treat seeds with hot water (50°C for 25 min).",
            "Rotate peppers with non-solanaceous crops for minimum 2 years."
        ]
    },
    "Pepper,_bell___healthy": {
        "plant": "Bell Pepper",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Pepper foliage is healthy, showing bright green leaves with blossoms and setting fruit.",
        "symptoms": ["Uniform green leaves with smooth margins and no lesions or curling."],
        "organic_remedies": ["Mulch with organic straw and feed with fish emulsion/compost."],
        "chemical_remedies": ["None needed."],
        "prevention": ["Maintain consistent watering to avoid blossom end rot and fungal issues."]
    },
    "Potato___Early_blight": {
        "plant": "Potato",
        "disease": "Early Blight",
        "is_healthy": False,
        "severity": "Moderate to High",
        "pathogen": "Alternaria solani (Fungus)",
        "summary": "Common foliar disease marked by concentric 'target-board' rings on older leaves.",
        "symptoms": [
            "Dark brown to black spots with concentric rings resembling a target or bullseye.",
            "Yellowing (chlorosis) surrounding the spots.",
            "Older lower leaves wither, die, and drop first."
        ],
        "organic_remedies": [
            "Spray copper soap or copper hydroxide at first appearance of target spots.",
            "Apply aerated compost tea to encourage beneficial leaf microflora."
        ],
        "chemical_remedies": [
            "Apply Chlorothalonil, Mancozeb, or Azoxystrobin on 7-14 day schedule during warm, humid conditions."
        ],
        "prevention": [
            "Ensure balanced nitrogen fertility; stressed plants are significantly more susceptible.",
            "Destroy potato vine debris post-harvest and rotate crops for 3 years."
        ]
    },
    "Potato___Late_blight": {
        "plant": "Potato",
        "disease": "Late Blight",
        "is_healthy": False,
        "severity": "Critical",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "summary": "Historic cause of the Irish Potato Famine; an extremely fast-spreading pathogen capable of destroying entire fields in days.",
        "symptoms": [
            "Water-soaked dark lesions spreading rapidly across leaves and stems.",
            "Delicate white fungal-like fuzz on undersides of leaves during humid mornings.",
            "Foul odor in fields as foliage rots and collapses.",
            "Brownish granular dry rot on potato tubers."
        ],
        "organic_remedies": [
            "Apply fixed copper sprays proactively prior to high-humidity rain periods.",
            "Immediately harvest and bury/destroy infected vines before spores wash into soil."
        ],
        "chemical_remedies": [
            "Apply systemic fungicides: Cymoxanil, Dimethomorph, Fluopicolide, or Mefenoxam."
        ],
        "prevention": [
            "Plant certified disease-free seed tubers.",
            "Avoid overhead irrigation; hill potatoes well with soil to shield tubers from spores."
        ]
    },
    "Potato___healthy": {
        "plant": "Potato",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Potato canopy shows lush foliage, sturdy stems, and no signs of blight or chlorosis.",
        "symptoms": ["Crisp, broad green leaves with active vegetative growth."],
        "organic_remedies": ["Apply balanced organic fertilizer high in potassium and phosphorus."],
        "chemical_remedies": ["None required."],
        "prevention": ["Hill soil around stems regularly and maintain consistent moisture."]
    },
    "Raspberry___healthy": {
        "plant": "Raspberry",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Canes and foliage are strong, green, and completely free of fungal spots or rusts.",
        "symptoms": ["Vibrant serrated leaves, upright canes, and no discoloration."],
        "organic_remedies": ["Mulch with wood chips and fertilize with aged organic compost."],
        "chemical_remedies": ["None required."],
        "prevention": ["Prune old floricanes after fruiting to maintain airflow."]
    },
    "Soybean___healthy": {
        "plant": "Soybean",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Trifoliate leaves are healthy, deep green, and nodulating effectively.",
        "symptoms": ["Uniform green trifoliate leaves without yellow mosaic or necrotic spotting."],
        "organic_remedies": ["Inoculate seeds with Bradyrhizobium japonicum for organic nitrogen fixation."],
        "chemical_remedies": ["None needed."],
        "prevention": ["Scout periodically for soybean aphid and rust."]
    },
    "Squash___Powdery_mildew": {
        "plant": "Squash / Zucchini",
        "disease": "Powdery Mildew",
        "is_healthy": False,
        "severity": "Moderate to High",
        "pathogen": "Podosphaera xanthii (Fungus)",
        "summary": "Flour-like white coating covering squash leaves, causing premature yellowing and drying out.",
        "symptoms": [
            "White talcum-powder-like fungal patches on leaf surfaces and stems.",
            "Leaves turn yellow, brown, curl upwards, and eventually crisp up.",
            "Reduced fruit yield and sunburned squash fruits due to loss of foliage shield."
        ],
        "organic_remedies": [
            "Spray diluted milk solution (35% milk, 65% water) weekly on leaves in sunlight.",
            "Apply potassium bicarbonate (1 tbsp/gallon) with horticultural oil.",
            "Use neem oil or sulfur before heavy spread."
        ],
        "chemical_remedies": [
            "Apply Myclobutanil, Trifloxystrobin, or Chlorothalonil early in disease progression."
        ],
        "prevention": [
            "Plant resistant squash cultivars (e.g., PMR hybrids).",
            "Give ample spacing between squash vines (3-4 feet apart) for maximum air flow."
        ]
    },
    "Strawberry___Leaf_scorch": {
        "plant": "Strawberry",
        "disease": "Leaf Scorch",
        "is_healthy": False,
        "severity": "Moderate",
        "pathogen": "Diplocarpon earlianum (Fungus)",
        "summary": "Foliar disease producing purple-to-brown irregular blotches, making leaves appear scorched or burned.",
        "symptoms": [
            "Numerous small, purplish spots on upper leaf surfaces that enlarge and turn dark brown.",
            "Leaves dry out, curl up, and take on a burnt/scorched appearance.",
            "Calyx (green cap on fruit) turns brown, affecting fruit marketability."
        ],
        "organic_remedies": [
            "Mow and remove old strawberry leaves after renovation/harvest.",
            "Spray liquid copper or bio-fungicide (Bacillus amyloliquefaciens)."
        ],
        "chemical_remedies": [
            "Apply Captan, Thiophanate-methyl, or Pyraclostrobin during spring growth."
        ],
        "prevention": [
            "Plant in full sun with well-drained soil on raised beds.",
            "Avoid overhead irrigation; use drip tape underneath plastic mulch."
        ]
    },
    "Strawberry___healthy": {
        "plant": "Strawberry",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Strawberry crowns and runners are vigorous with rich green foliage and clean blossoms.",
        "symptoms": ["Tri-leaflet foliage is vibrant green, firm, and unspotted."],
        "organic_remedies": ["Apply pine straw mulch and organic balanced berry fertilizer."],
        "chemical_remedies": ["None required."],
        "prevention": ["Keep fruit elevated from wet soil with mulch and rotate beds every 3 years."]
    },
    "Tomato___Bacterial_spot": {
        "plant": "Tomato",
        "disease": "Bacterial Spot",
        "is_healthy": False,
        "severity": "High",
        "pathogen": "Xanthomonas spp. (Bacteria)",
        "summary": "Warm-season bacterial disease causing dark water-soaked spots on leaves and scabby raised spots on tomatoes.",
        "symptoms": [
            "Small (1/8 inch), water-soaked, dark brown or black angular leaf spots.",
            "Leaves turn yellow around spots, then scorch and fall off.",
            "Small raised scab-like rough brown spots on green fruit."
        ],
        "organic_remedies": [
            "Apply fixed copper combined with Bacillus subtilis early in the morning.",
            "Mulch heavily beneath tomato plants to prevent soil bacteria from splashing onto foliage."
        ],
        "chemical_remedies": [
            "Spray Copper Hydroxide tank-mixed with Mancozeb for synergized control."
        ],
        "prevention": [
            "Use certified disease-free seed or hot-water-treat seeds.",
            "Do not work in tomato patches when vines are wet."
        ]
    },
    "Tomato___Early_blight": {
        "plant": "Tomato",
        "disease": "Early Blight",
        "is_healthy": False,
        "severity": "Moderate to High",
        "pathogen": "Alternaria solani (Fungus)",
        "summary": "Classic target-spot foliar disease starting on bottom leaves and progressing upwards.",
        "symptoms": [
            "Dark brown spots with concentric target-board rings on older foliage.",
            "Leaves yellow around spots, turn brown, and drop, exposing tomatoes to sunscald.",
            "Dark, sunken, leathery cankers on stems and fruit stem-ends."
        ],
        "organic_remedies": [
            "Prune off the lowest 12-18 inches of branches to prevent splash infection.",
            "Spray organic copper fungicide or Serenade (Bacillus subtilis).",
            "Apply thick straw or plastic mulch around base of plant."
        ],
        "chemical_remedies": [
            "Apply Chlorothalonil (Daconil), Mancozeb, or Azoxystrobin every 7-10 days."
        ],
        "prevention": [
            "Rotate tomato location every 2-3 years away from potatoes, peppers, and eggplants.",
            "Stake or cage tomatoes for upright growth and maximum air circulation."
        ]
    },
    "Tomato___Late_blight": {
        "plant": "Tomato",
        "disease": "Late Blight",
        "is_healthy": False,
        "severity": "Critical",
        "pathogen": "Phytophthora infestans (Oomycete)",
        "summary": "Fast-moving water-mold disease that can destroy whole tomato plants within days in cool, wet weather.",
        "symptoms": [
            "Large, dark, water-soaked oily lesions spreading on leaves and stems.",
            "White fungal bloom on leaf undersides in humid conditions.",
            "Golden-brown, firm, greasy-looking rot on green or ripe tomatoes.",
            "Rapid plant collapse resembling frost damage."
        ],
        "organic_remedies": [
            "Apply preventive copper spray before rainy spells when temperatures are between 60-75°F (15-24°C).",
            "Remove and immediately bag/dispose of entire infected plants; do NOT compost them."
        ],
        "chemical_remedies": [
            "Apply systemic fungicides: Chlorothalonil, Cymoxanil (Curzate), or Mandipropamid."
        ],
        "prevention": [
            "Plant late blight-resistant varieties (e.g., Mountain Magic, Defiant, Plum Regal).",
            "Monitor regional late blight tracking maps and forecasts."
        ]
    },
    "Tomato___Leaf_Mold": {
        "plant": "Tomato",
        "disease": "Leaf Mold",
        "is_healthy": False,
        "severity": "Moderate",
        "pathogen": "Passalora fulva (Fungus)",
        "summary": "Foliar disease prevalent in greenhouses and high tunnels under high relative humidity (>85%).",
        "symptoms": [
            "Pale greenish-yellow indistinct spots on upper leaf surfaces.",
            "Olive-green to velvety brown mold growth on lower leaf surfaces.",
            "Infected leaves curl, wither, and drop prematurely."
        ],
        "organic_remedies": [
            "Increase ventilation and airflow in greenhouses with exhaust fans and louvers.",
            "Apply biofungicides containing Bacillus amyloliquefaciens or copper octanoate."
        ],
        "chemical_remedies": [
            "Apply Chlorothalonil, Mancozeb, or Difenoconazole at first symptom onset."
        ],
        "prevention": [
            "Keep greenhouse relative humidity below 85% with night heating and venting.",
            "Space plants adequately and prune lower suckers."
        ]
    },
    "Tomato___Septoria_leaf_spot": {
        "plant": "Tomato",
        "disease": "Septoria Leaf Spot",
        "is_healthy": False,
        "severity": "Moderate to High",
        "pathogen": "Septoria lycopersici (Fungus)",
        "summary": "Very common tomato fungal disease producing tiny circular spots with grey centers and dark borders.",
        "symptoms": [
            "Numerous small (1/16 to 1/8 inch) circular spots with grayish-white centers and dark brown margins.",
            "Tiny black specks (pycnidia) visible inside the gray center with a hand lens.",
            "Severe yellowing and dropping of lower leaves working upwards."
        ],
        "organic_remedies": [
            "Prune off infected lower leaves immediately upon identification.",
            "Apply copper sulfate or liquid copper spray every 7-10 days.",
            "Apply heavy mulch to stop soil splashing."
        ],
        "chemical_remedies": [
            "Spray Chlorothalonil, Mancozeb, or Pyraclostrobin beginning at transplanting or first spot appearance."
        ],
        "prevention": [
            "Water with soaker hoses or drip irrigation exclusively; keep foliage bone dry.",
            "Clean up all tomato garden debris thoroughly at the end of the season."
        ]
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "plant": "Tomato",
        "disease": "Spider Mites (Two-Spotted)",
        "is_healthy": False,
        "severity": "High",
        "pathogen": "Tetranychus urticae (Arachnid Pest)",
        "summary": "Microscopic sap-sucking pests thriving in hot, dry conditions, forming fine silk webbing and yellow speckling.",
        "symptoms": [
            "Fine yellow or white stippling (speckling) across leaf surfaces.",
            "Fine silk webbing on leaf undersides and branch crotches.",
            "Leaves turn bronze or yellow, dry up, and drop; plant vigor severely declines."
        ],
        "organic_remedies": [
            "Spray undersides of leaves with insecticidal soap or horticultural neem oil.",
            "Release predatory mites (Phytoseiulus persimilis or Neoseiulus californicus).",
            "Blast undersides of leaves with strong jet of water to knock down populations."
        ],
        "chemical_remedies": [
            "Apply specific miticides like Bifenazate, Abamectin, or Spiromesifen (avoid general pyrethroids which kill predators)."
        ],
        "prevention": [
            "Keep soil well hydrated and prevent dusty conditions around garden borders.",
            "Regularly inspect leaf undersides with a 10x magnifying hand lens."
        ]
    },
    "Tomato___Target_Spot": {
        "plant": "Tomato",
        "disease": "Target Spot",
        "is_healthy": False,
        "severity": "Moderate",
        "pathogen": "Corynespora cassiicola (Fungus)",
        "summary": "Fungal pathogen causing target-ring spots on leaves, stems, and sunken pits on fruit.",
        "symptoms": [
            "Pinpoint brown spots enlarging to circular lesions with pale brown centers and concentric rings.",
            "Yellow halos around spots on leaves.",
            "Sunken, crater-like brown lesions on green and ripe tomato fruit."
        ],
        "organic_remedies": [
            "Apply copper-based fungicides with biofungicides.",
            "Maintain wide plant spacing to facilitate rapid drying after rains."
        ],
        "chemical_remedies": [
            "Spray Azoxystrobin, Chlorothalonil, or Boscalid."
        ],
        "prevention": [
            "Avoid overhead irrigation.",
            "Eliminate solanaceous weeds (nightshades) nearby that harbor the fungus."
        ]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "plant": "Tomato",
        "disease": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "is_healthy": False,
        "severity": "Critical",
        "pathogen": "Begomovirus (Transmitted by Silverleaf Whitefly)",
        "summary": "Viral disease transmitted by whiteflies; causes extreme stunting, leaf curling, and severe loss of yield.",
        "symptoms": [
            "Upward cupping and curling of leaf margins.",
            "Marked yellowing (chlorosis) along leaf edges and between veins.",
            "Stunted, bushy upright plant growth; flowers abort and drop before fruit set."
        ],
        "organic_remedies": [
            "Hang yellow sticky cards around crops to trap and monitor whitefly vectors.",
            "Spray insecticidal soap or horticultural oil weekly to kill whitefly nymphs.",
            "Immediately pull up and destroy virus-infected plants; viral plants cannot be cured."
        ],
        "chemical_remedies": [
            "Manage whitefly vectors with Imidacloprid, Dinotefuran, or Spiromesifen."
        ],
        "prevention": [
            "Plant TYLCV-resistant tomato cultivars (e.g., Tycoon, Camaro, Chef's Choice).",
            "Use fine mesh insect netting (50-mesh) on nursery seedlings and greenhouse vents."
        ]
    },
    "Tomato___Tomato_mosaic_virus": {
        "plant": "Tomato",
        "disease": "Tomato Mosaic Virus (ToMV)",
        "is_healthy": False,
        "severity": "High",
        "pathogen": "Tobamovirus (Mechanically transmitted & seedborne)",
        "summary": "Extremely stable, persistent virus easily spread by mechanical handling, pruning shears, and clothing.",
        "symptoms": [
            "Mottled light and dark green mosaic patterns on leaves.",
            "Distorted, blistered, or narrow strap-like 'fern-leaf' foliage.",
            "Stunted plant growth and uneven ripening or internal browning of fruit."
        ],
        "organic_remedies": [
            "Dip hands and pruning tools in non-fat dry milk solution (20% milk) while handling plants.",
            "Carefully remove and dispose of infected plants to avoid touching adjacent healthy plants."
        ],
        "chemical_remedies": [
            "No chemical virucide exists. Management focuses solely on hygiene and eradication."
        ],
        "prevention": [
            "Do not smoke or use tobacco products near tomato plants (tobacco can harbor related viruses).",
            "Disinfect stakes, pots, and gardening tools with 10% bleach or trisodium phosphate (TSP).",
            "Plant certified ToMV-resistant cultivars (marked with 'T' or 'ToMV' on seed packet)."
        ]
    },
    "Tomato___healthy": {
        "plant": "Tomato",
        "disease": "Healthy Plant",
        "is_healthy": True,
        "severity": "None",
        "pathogen": "None (Plant is healthy)",
        "summary": "Tomato foliage is vigorous, dark green, aromatic, and free from pathogenic spots or pest infestations.",
        "symptoms": ["Lush, sturdy pinnate leaves with bright blossoms and developing green fruit."],
        "organic_remedies": ["Feed with balanced organic tomato fertilizer rich in calcium and potassium."],
        "chemical_remedies": ["None required."],
        "prevention": ["Mulch base, stake plants securely, and water deeply at soil level."]
    }
}


def get_disease_details(raw_class_name: str) -> Dict[str, Any]:
    """
    Returns rich information about a given disease class.
    Falls back gracefully if an unexpected class name is supplied.
    """
    if raw_class_name in DISEASE_KNOWLEDGE_BASE:
        return DISEASE_KNOWLEDGE_BASE[raw_class_name]
    
    # Generic fallback parser
    parts = raw_class_name.split("___")
    plant = parts[0].replace("_", " ") if len(parts) > 0 else "Unknown Plant"
    disease = parts[1].replace("_", " ") if len(parts) > 1 else "Unknown Condition"
    is_healthy = "healthy" in disease.lower()
    
    return {
        "plant": plant,
        "disease": "Healthy" if is_healthy else disease,
        "is_healthy": is_healthy,
        "severity": "None" if is_healthy else "Moderate",
        "pathogen": "None" if is_healthy else "Fungal/Bacterial pathogen",
        "summary": f"{plant} showing {disease}.",
        "symptoms": ["No specific symptoms recorded for this variant."] if is_healthy else ["Leaf spotting or discoloration."],
        "organic_remedies": ["Maintain optimal plant nutrition and soil moisture."],
        "chemical_remedies": ["Consult a local agricultural extension specialist."],
        "prevention": ["Practice regular crop hygiene and clean irrigation."]
    }
