import pandas as pd

translations = {
    'Artistique': 'Art',
    'Montage image': 'Picture Editing',
    'Assistant.es réalisateur.trices': 'Assistant Director',
    'Lieux de tournage': 'Locations',
    'Coordonnateur.trices de production': 'Production Coordinators',
    'Assistant.es de production': 'Production Assistant',
    'Réalisateur.trices': 'Director',
    "Réalisateur.trices": "Director",
    'Région Maritimes': 'Maritimes',
    'Quebec': 'Québec',
    'm': 'M',
    'f': 'F',
    'pnd': 'PND',
    'gnc': 'GNC',
    'Oui, beaucoup': 'Yes, very much', 
    'Pas du tout.': 'Not at all', 
    'Oui, parfois': 'Yes, sometimes',
    'Non, pas vraiment.': 'No, not really',
    'Oui, un peu.': 'Yes, a little',
    'Souvent (au moins une fois par mois)': 'Often (at least once a month)', 
    'Jamais': 'Never', 
    'Tous les jours': 'Every Day',
    'Rarement': 'Rarely', 
    'Très souvent (au moins une fois par semaine)': 'Very Often (at least once a week)',
    'Je n’utilise pas d’IA ou d’IA générative': 'I do not use AI',
    'Par nécessité pour rester compétitif·ve': 'By necessity to stay competitive',
    'Par choix personnel': 'By personal choice',
    'En raison de la pression des pairs': 'By peer pressure',
    'Parce que la production l’exige': "Because it's required by the production",
    "J’en ai entendu parler – J’ai entendu parler en général de ce type d’outil utilisé pour le travail de production.": 'Heard About It',
    "Je n’en ai jamais entendu parler – Je n’ai pas entendu parler de l’utilisation de ce type d’outil dans le domaine cinématographique et télévisuel.": 'Never Heard Of It',
    "Que dans les médias – J’ai vu ou entendu des reportages dans les médias sur l’utilisation de ce type d’outil dans le domaine cinématographique et télévisuel.": 'Media Only',
    "Je l’ai utilisé – J’ai personnellement utilisé ce type d’outil pour mon travail de production.": 'Used It',
    "Je le connais – Je connais une personne ou une entreprise spécifique qui utilise ce type d’outil pour le travail de production.": 'Know About It',
    'Peu inquiet·ète': 'Somewhat concerned',
    'Assez inquiet·ète': 'Mostly unconcerned', 
    'Pas inquiet·ète du tout': 'Not concerned at all',
    'Pas du tout inquiet·ète': 'Not concerned at all',
    'Très inquiet·ète': 'Very concerned',
    'Pas très inquiet·ète': 'Not very concerned',
    'Oui': 'Yes',
    'Non': 'No',
    'Non, mais j’aimerais suivre une formation sur cet outil ou une alternative similaire': 'No, but I would like to attend training on this tool or a similar alternative.',
    'Non, et ce genre de formation ne m’intéresse pas': 'No, and I have no interest in such training.',
    'Non, mais je prévois de suivre une formation sur cet outil ou une alternative similaire': "No, but I'm planning to attend training on this tool or a similar alternative.",
    "Non, l'IA générative ne complémente pas mon rôle.": 'No, Generative AI does not complement my role',
    "L'IA générative complémente parfaitement mon rôle.": 'Generative AI perfectly complements my role',
    'Je ne sais pas.': "I don't know",
    "L'IA générative m'aide dans certaines de mes tâches.": 'Generative AI helps with some of my tasks',
    "L'IA générative peut parfois aider.": 'Generative AI can help sometimes',
}

df = pd.read_excel('data/AI-Survey-Results-tr.xlsx')
df.replace(translations, inplace=True)
df_tr = df
df_tr.to_excel('data/AI-Survey-Results-tr.xlsx')

# Creating income bracket column
df = pd.read_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr.xlsx')
bins = [0, 50001, 100001, 150000, 200000, 1000000]
brackets = ['Under $50k', '50k-100k', '100k-150k', '150k-200k', 'Over $200k']
df['Income_Bracket'] = pd.cut(df['Incomes_last_12_mths'], bins=bins, labels=brackets)
df.insert(11, 'Income_Bracket', df['Income_Bracket'], allow_duplicates=True)
df = df.iloc[:, 0:254]
df.to_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr.xlsx')

# Getting column indexes for creating tasks and tools dataframes
column_info = pd.DataFrame({
    'Column_Name': df.columns,
    'Index_Number': range(len(df.columns))
})
column_info.to_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Index.xlsx')

# Creating tasks and tools dataframes
id_variables = ['id', 'Language', 'Primary Job', 'Secondary Job', 'District Council',
       'Ethnicity-Broad', 'FM_Primary_Job', 'FM_Secondary_Job', 'FM_Sex',
       'FM_Age', 'Income_Bracket']


# Replace the full tool questions with the specific AI Tool name
replacement_dict = {
    "Have you used any of the following tools to assist with your job as in the Director caucus? (Runway ML: Allows directors to experiment with real-time visual effects and style transfers, enabling quick visualization of ideas during pre-production or post-production.)": "Runway ML",
    "Have you used any of the following tools to assist with your job as in the Director caucus? (Runway ML: Allows directors to experiment with real-time visual effects and style transfers, enabling quick visualization of ideas during pre-production or post-production.)": "Runway ML",
    "Have you used any of the following tools to assist with your job as in the Director caucus? (ChatGPT (OpenAI): Scriptwriting assistance, brainstorming ideas, and dialogue generation.)": "ChatGPT",
    "Have you used any of the following tools to assist with your job as in the Director caucus? (Synthesia: Generate AI-driven video content or virtual actors for pre-visualization and concept testing.)": "Synthesia",
    "Have you used any of the following tools to assist with your job as in the Director caucus? (DALL-E 3: Generate detailed concept art and storyboarding from textual descriptions.)": "DALL-E 3",
    "Have you used any of the following tools to assist with your job as in the Director caucus? (DALL-E 3: Generate detailed concept art and storyboarding from textual descriptions.)": "DALL-E 3",
    "Have you used any of the following tools to assist with your job in the Assistant Director caucus? (Notion AI: Helps ADs manage schedules, create to-do lists, and automate task management for smoother shoot coordination.)": "Notion AI",
    "Have you used any of the following tools to assist with your job in the Assistant Director caucus? (Sunsama: AI-powered planning and task management for organizing production schedules, call sheets, and breakdowns.)": "Sunsama",
    "Have you used any of the following tools to assist with your job in the Assistant Director caucus? (Calendly + Zapier AI integration: Streamline scheduling meetings, location scouting, and time management.)": "Calendly + Zapier AI",
    "Have you used any of the following tools to assist with your job in the Assistant Director caucus? (StudioBinder: Automates the creation and distribution of call sheets, shooting schedules, and production reports, allowing coordinators to save time and streamline communication.)": "StudioBinder",
    "Have you used any of the following tools to assist with your job in the Assistant Director caucus? (Movie Magic Scheduling (AI-enhanced features): AI helps optimize scheduling and resource planning, making it easier to coordinate crew, equipment, and locations.)": "Movie Magic Scheduling",
    "Have you used any of the following tools to assist with your work in the Art Department? (MidJourney: For creating mood boards, production design concepts, and reference images with detailed visualizations of scenes, sets, and props.)": "MidJourney",
    "Have you used any of the following tools to assist with your work in the Art Department? (Shapr3D: AI-powered 3D modeling and design software for pre-visualizing set designs.)": "Shapr3D",
    "Have you used any of the following tools to assist with your work in the Art Department? (DALL·E 3: To generate custom images of props, set ideas, and costumes based on textual inputs.)": "DALL·E 3",
    "Have you used any of the following tools to assist with your work in the Art Department? (Artbreeder: AI-assisted tool for designing character and mood concepts, as well as set backgrounds.)": "Artbreeder",
    "Have you used any of the following tools to assist with your work in post production? (Adobe Premiere Pro (Sensei AI): Automates tasks such as cutting, color matching, and sound mixing with AI-powered features. Also has an auto-tagging footage feature.)": "Adobe Premiere Pro",
    "Have you used any of the following tools to assist with your work in post production? (Descript: AI-powered audio and video editor, useful for transcription, text-based video editing, and sound clean-up.)": "Descript",
    "Have you used any of the following tools to assist with your work in post production? (Runway ML: For AI-assisted VFX, including green screen replacement, rotoscoping, and video inpainting.)": "Runway ML",
    "Have you used any of the following tools to assist with your work in post production? (Audionamix: AI-based audio separation tool to clean up dialogue, music, or sound effects.)": "Audionamix",
    "Have you used any of the following tools to assist with your work in post production? (Blackmagic Design DaVinci Resolve (with Neural Engine): AI-enhanced color grading, motion tracking, and facial recognition.)": "DaVinci Resolve",
    "Have you used any of the following tools to assist with your work in the Locations department? (Location Scout AI (various tools like Scouting Cloud): AI tools for scouting locations by uploading photos and receiving location matches based on the production's needs.)": "Location Scout AI",
    "Have you used any of the following tools to assist with your work in the Locations department? (Google Earth Studio: AI-powered 3D animation tool for visualizing potential locations and camera movements.)": "Google Earth Studio",
    "Have you used any of the following tools to assist with your work in the Locations department? (What3Words + AI Integration: Helps location managers log and communicate precise locations using AI to optimize scouting logistics.)": "What3Words + AI",
    "Have you used any of the following tools in film & television production? (Movie Magic Scheduling (with AI add-ons): AI integration for better scheduling and resource allocation on film shoots.)": "Movie Magic Scheduling",
    "Have you used any of the following tools in film & television production? (StudioBinder: Helps create production timelines, shot lists, and call sheets with integrated AI tools to manage team collaboration and track logistics.)": "StudioBinder",
    "Have you used any of the following tools in film & television production? (Celtx: AI-powered scheduling and budgeting tools for streamlining production planning and task management.)": "Celtx",
    "Have you used any of the following tools in film & television production? (Trello (with Butler AI integration): Trello’s Butler AI automates repetitive tasks, like assigning team members, creating task lists, and setting deadlines based on project needs.)": "Trello’s Butler AI",
    "Have you used any of the following tools in film & television production? (Monday.com (AI-powered work OS): This platform offers AI automation for workflow tracking, task management, and resource allocation, ensuring production timelines are met.)": "Monday.com",
    "Have you used any of the following tools in film & television production? (Notion AI: Useful for managing production notes, team collaboration and generating meeting minutes or reports from key points.)": "Notion AI",
    "Have you used any of the following tools in film & television production? (QuickBooks (Smart Features): Automates accounting tasks, expense tracking, and payroll for productions.)": "QuickBooks",
    "Have you used any of the following tools in film & television production? (Xero: AI-driven accounting platform for tracking production budgets and automating invoicing.)": "Xero",
    "Have you used any of the following tools in film & television production? (Vic.ai: Provides AI-powered accounts payable automation, helping with financial data analysis and cost management.)": "Vic.ai",
    "Have you used any of the following tools in film & television production? (Expensify: AI automates expense reporting and reimbursement, making it useful for tracking production costs.)": "Expensify",
    "Have you used any of the following tools to assist with your job as in the Director caucus? (ChatGPT (OpenAI): Scriptwriting assistance, brainstorming ideas, and dialogue generation.)": "ChatGPT",
    "Have you used any of the following tools to assist with your job as in the Director caucus? (Synthesia: Generate AI-driven video content or virtual actors for pre-visualization and concept testing.)": "Synthesia",
    "Have you used any of the following tools to assist with your work in the Art Department? (Artbreeder: AI-assisted tool for designing character and mood concepts, as well as set backgrounds.)": "Artbreeder",
    "Have you used any of the following tools to assist with your work in the Locations department? (What3Words + AI Integration: Helps location managers log and communicate precise locations using AI to optimize scouting logistics. )": "What3Words + AI",
    "Have you used any of the following tools in film &amp; television production? (Movie Magic Scheduling (with AI add-ons): AI integration for better scheduling and resource allocation on film shoots.)": "Movie Magic Scheduling",
    "Have you used any of the following tools in film &amp; television production? (StudioBinder: Helps create production timelines, shot lists, and call sheets with integrated AI tools to manage team collaboration and track logistics.)": "StudioBinder",
    "Have you used any of the following tools in film &amp; television production? (Celtx: AI-powered scheduling and budgeting tools for streamlining production planning and task management.)": "Celtx",
    "Have you used any of the following tools in film &amp; television production? (Trello (with Butler AI integration): Trello’s Butler AI automates repetitive tasks, like assigning team members, creating task lists, and setting deadlines based on project needs.)": "Trello’s Butler AI",
    "Have you used any of the following tools in film &amp; television production? (Monday.com (AI-powered work OS): This platform offers AI automation for workflow tracking, task management, and resource allocation, ensuring production timelines are met.)": "Monday.com",
    "Have you used any of the following tools in film &amp; television production? (Notion AI: Useful for managing production notes, team collaboration and generating meeting minutes or reports from key points.)": "Notion AI",
    "Have you used any of the following tools in film &amp; television production? (QuickBooks (Smart Features): Automates accounting tasks, expense tracking, and payroll for productions.)": "QuickBooks",
    "Have you used any of the following tools in film &amp; television production? (Xero: AI-driven accounting platform for tracking production budgets and automating invoicing.)": "Xero",
    "Have you used any of the following tools in film &amp; television production? (Vic.ai: Provides AI-powered accounts payable automation, helping with financial data analysis and cost management.)": "Vic.ai"
}

others_replacement_dict = {
    "Do you know of other Directors who’ve used any of the following tools in film &amp; television production? (Runway ML: Allows directors to experiment with real-time visual effects and style transfers, enabling quick visualization of ideas during pre-production or post-production.)": "Runway ML",
    "Do you know of other Directors who’ve used any of the following tools in film &amp; television production? (ChatGPT (OpenAI): Scriptwriting assistance, brainstorming ideas, and dialogue generation.)": "ChatGPT (OpenAI)",
    "Do you know of other Directors who’ve used any of the following tools in film &amp; television production? (Synthesia: Generate AI-driven video content or virtual actors for pre-visualization and concept testing.)": "Synthesia",
    "Do you know of other Directors who’ve used any of the following tools in film &amp; television production? (DALL-E 3: Generate detailed concept art and storyboarding from textual descriptions.)": "DALL-E 3",
    "Do you know of other Assistant Directors who’ve used any of the following tools in film &amp; television production? (Notion AI: Helps ADs manage schedules, create to-do lists, and automate task management for smoother shoot coordination.)": "Notion AI",
    "Do you know of other Assistant Directors who’ve used any of the following tools in film &amp; television production? (Sunsama: AI-powered planning and task management for organizing production schedules, call sheets, and breakdowns.)": "Sunsama",
    "Do you know of other Assistant Directors who’ve used any of the following tools in film &amp; television production? (Calendly + Zapier AI integration: Streamline scheduling meetings, location scouting, and time management.)": "Calendly + Zapier AI integration",
    "Do you know of other Assistant Directors who’ve used any of the following tools in film &amp; television production? (StudioBinder: Automates the creation and distribution of call sheets, shooting schedules, and production reports, allowing coordinators to save time and streamline communication.)": "StudioBinder",
    "Do you know of other Assistant Directors who’ve used any of the following tools in film &amp; television production? (Movie Magic Scheduling (AI-enhanced features): AI helps optimize scheduling and resource planning, making it easier to coordinate crew, equipment, and locations.)": "Movie Magic Scheduling",
    "Do you know other Art Department members who’ve used any of the following tools in film &amp; television production? (MidJourney: For creating mood boards, production design concepts, and reference images with detailed visualizations of scenes, sets, and props.)": "MidJourney",
    "Do you know other Art Department members who’ve used any of the following tools in film &amp; television production? (Shapr3D: AI-powered 3D modeling and design software for pre-visualizing set designs.)": "Shapr3D",
    "Do you know other Art Department members who’ve used any of the following tools in film &amp; television production? (DALL·E 3: To generate custom images of props, set ideas, and costumes based on textual inputs.)": "DALL·E 3",
    "Do you know other Art Department members who’ve used any of the following tools in film &amp; television production? (Artbreeder: AI-assisted tool for designing character and mood concepts, as well as set backgrounds.)": "Artbreeder",
    "Do you know of others who've used the following tools in film &amp; television post production? (Adobe Premiere Pro (Sensei AI): Automates tasks such as cutting, color matching, and sound mixing with AI-powered features. Also has an auto-tagging footage feature.)": "Adobe Premiere Pro (Sensei AI)",
    "Do you know of others who've used the following tools in film &amp; television post production? (Descript: AI-powered audio and video editor, useful for transcription, text-based video editing, and sound clean-up.)": "Descript",
    "Do you know of others who've used the following tools in film &amp; television post production? (Runway ML: For AI-assisted VFX, including green screen replacement, rotoscoping, and video inpainting.)": "Runway ML",
    "Do you know of others who've used the following tools in film &amp; television post production? (Audionamix: AI-based audio separation tool to clean up dialogue, music, or sound effects.)": "Audionamix",
    "Do you know of others who've used the following tools in film &amp; television post production? (Blackmagic Design DaVinci Resolve (with Neural Engine): AI-enhanced color grading, motion tracking, and facial recognition.)": "Blackmagic Design DaVinci Resolve",
    "Do you know of other Locations personnel who've used the following tools in film &amp; television production? (Location Scout AI (various tools like Scouting Cloud): AI tools for scouting locations by uploading photos and receiving location matches based on the production's needs.)": "Location Scout AI",
    "Do you know of other Locations personnel who've used the following tools in film &amp; television production? (Google Earth Studio: AI-powered 3D animation tool for visualizing potential locations and camera movements.)": "Google Earth Studio",
    "Do you know of other Locations personnel who've used the following tools in film &amp; television production? (What3Words + AI Integration: Helps location managers log and communicate precise locations using AI to optimize scouting logistics.)": "What3Words + AI Integration",
    "Do you know of others who've used any of the following tools in film &amp; television production? (Movie Magic Scheduling (with AI add-ons): AI integration for better scheduling and resource allocation on film shoots.)": "Movie Magic Scheduling",
    "Do you know of others who've used any of the following tools in film &amp; television production? (StudioBinder: Helps create production timelines, shot lists, and call sheets with integrated AI tools to manage team collaboration and track logistics.)": "StudioBinder",
    "Do you know of others who've used any of the following tools in film &amp; television production? (Celtx: AI-powered scheduling and budgeting tools for streamlining production planning and task management.)": "Celtx",
    "Do you know of others who've used any of the following tools in film &amp; television production? (Trello (with Butler AI integration): Trello’s Butler AI automates repetitive tasks, like assigning team members, creating task lists, and setting deadlines based on project needs.)": "Trello (Butler AI integration)",
    "Do you know of others who've used any of the following tools in film &amp; television production? (Monday.com (AI-powered work OS): This platform offers AI automation for workflow tracking, task management, and resource allocation, ensuring production timelines are met.)": "Monday.com",
    "Do you know of others who've used any of the following tools in film &amp; television production? (Notion AI: Useful for managing production notes, team collaboration and generating meeting minutes or reports from key points.)": "Notion AI",
    "Do you know of others who've used any of the following tools in film &amp; television production? (QuickBooks (Smart Features): Automates accounting tasks, expense tracking, and payroll for productions.)": "QuickBooks",
    "Do you know of others who've used any of the following tools in film &amp; television production? (Xero: AI-driven accounting platform for tracking production budgets and automating invoicing.)": "Xero",
    "Do you know of others who've used any of the following tools in film &amp; television production? (Vic.ai: Provides AI-powered accounts payable automation, helping with financial data analysis and cost management.)": "Vic.ai",
    "Do you know of others who've used any of the following tools in film &amp; television production? (Expensify: AI automates expense reporting and reimbursement, making it useful for tracking production costs.)": "Expensify",
    "Do you know of other Directors who’ve used any of the following tools in film &amp; television production? (Runway ML: Allows directors to experiment with real-time visual effects and style transfers, enabling quick visualization of ideas during pre-production or post-production.)": "Runway ML",
    "Do you know of other Directors who’ve used any of the following tools in film &amp; television production? (ChatGPT (OpenAI): Scriptwriting assistance, brainstorming ideas, and dialogue generation.)": "ChatGPT (OpenAI)",
    "Do you know of other Directors who’ve used any of the following tools in film &amp; television production? (Synthesia: Generate AI-driven video content or virtual actors for pre-visualization and concept testing.)": "Synthesia",
    "Do you know of other Directors who’ve used any of the following tools in film &amp; television production? (DALL-E 3: Generate detailed concept art and storyboarding from textual descriptions.)": "DALL-E 3",
    "Do you know other Art Department members who’ve used any of the following tools in film &amp; television production? (Artbreeder: AI-assisted tool for designing character and mood concepts, as well as set backgrounds.)": "Artbreeder",
    "Do you know of other Locations personnel who've used the following tools in film &amp; television production? (What3Words + AI Integration: Helps location managers log and communicate precise locations using AI to optimize scouting logistics. )": "What3Words + AI Integration"
}


training_replacement_dict = {
    "Do you have training on any of these tools? (Runway ML: Allows directors to experiment with real-time visual effects and style transfers, enabling quick visualization of ideas during pre-production or post-production.)": "Runway ML",
    "Do you have training on any of these tools? (ChatGPT (OpenAI): Scriptwriting assistance, brainstorming ideas, and dialogue generation.)": "ChatGPT (OpenAI)",
    "Do you have training on any of these tools? (Synthesia: Generate AI-driven video content or virtual actors for pre-visualization and concept testing.)": "Synthesia",
    "Do you have training on any of these tools? (DALL-E 3: Generate detailed concept art and storyboarding from textual descriptions.)": "DALL-E 3",
    "Do you have training on any of these tools? (Notion AI: Helps ADs manage schedules, create to-do lists, and automate task management for smoother shoot coordination.)": "Notion AI",
    "Do you have training on any of these tools? (Sunsama: AI-powered planning and task management for organizing production schedules, call sheets, and breakdowns.)": "Sunsama",
    "Do you have training on any of these tools? (Calendly + Zapier AI integration: Streamline scheduling meetings, location scouting, and time management.)": "Calendly + Zapier AI integration",
    "Do you have training on any of these tools? (StudioBinder: Automates the creation and distribution of call sheets, shooting schedules, and production reports, allowing coordinators to save time and streamline communication.)": "StudioBinder",
    "Do you have training on any of these tools? (Movie Magic Scheduling (AI-enhanced features): AI helps optimize scheduling and resource planning, making it easier to coordinate crew, equipment, and locations.)": "Movie Magic Scheduling",
    "Do you have training on any of these tools? (MidJourney: For creating mood boards, production design concepts, and reference images with detailed visualizations of scenes, sets, and props.)": "MidJourney",
    "Do you have training on any of these tools? (Shapr3D: AI-powered 3D modeling and design software for pre-visualizing set designs.)": "Shapr3D",
    "Do you have training on any of these tools? (DALL·E 3: To generate custom images of props, set ideas, and costumes based on textual inputs.)": "DALL·E 3",
    "Do you have training on any of these tools? (Artbreeder: AI-assisted tool for designing character and mood concepts, as well as set backgrounds.)": "Artbreeder",
    "Do you have training on any of these tools? (Adobe Premiere Pro (Sensei AI): Automates tasks such as cutting, color matching, and sound mixing with AI-powered features. Also has an auto-tagging footage feature.)": "Adobe Premiere Pro (Sensei AI)",
    "Do you have training on any of these tools? (Descript: AI-powered audio and video editor, useful for transcription, text-based video editing, and sound clean-up.)": "Descript",
    "Do you have training on any of these tools? (Runway ML: For AI-assisted VFX, including green screen replacement, rotoscoping, and video inpainting.)": "Runway ML",
    "Do you have training on any of these tools? (Audionamix: AI-based audio separation tool to clean up dialogue, music, or sound effects.)": "Audionamix",
    "Do you have training on any of these tools? (Blackmagic Design DaVinci Resolve (with Neural Engine): AI-enhanced color grading, motion tracking, and facial recognition.)": "Blackmagic Design DaVinci Resolve",
    "Do you have training on any of these tools? (Location Scout AI (various tools like Scouting Cloud): AI tools for scouting locations by uploading photos and receiving location matches based on the production's needs.)": "Location Scout AI",
    "Do you have training on any of these tools? (Google Earth Studio: AI-powered 3D animation tool for visualizing potential locations and camera movements.)": "Google Earth Studio",
    "Do you have training on any of these tools? (What3Words + AI Integration: Helps location managers log and communicate precise locations using AI to optimize scouting logistics.)": "What3Words + AI Integration",
    "Do you have training on any of these tools? (Movie Magic Scheduling (with AI add-ons): AI integration for better scheduling and resource allocation on film shoots.)": "Movie Magic Scheduling",
    "Do you have training on any of these tools? (StudioBinder: Helps create production timelines, shot lists, and call sheets with integrated AI tools to manage team collaboration and track logistics.)": "StudioBinder",
    "Do you have training on any of these tools? (Celtx: AI-powered scheduling and budgeting tools for streamlining production planning and task management.)": "Celtx",
    "Do you have training on any of these tools? (Trello (with Butler AI integration): Trello’s Butler AI automates repetitive tasks, like assigning team members, creating task lists, and setting deadlines based on project needs.)": "Trello (Butler AI integration)",
    "Do you have training on any of these tools? (Monday.com (AI-powered work OS): This platform offers AI automation for workflow tracking, task management, and resource allocation, ensuring production timelines are met.)": "Monday.com",
    "Do you have training on any of these tools? (Notion AI: Useful for managing production notes, team collaboration and generating meeting minutes or reports from key points.)": "Notion AI",
    "Do you have training on any of these tools? (QuickBooks (Smart Features): Automates accounting tasks, expense tracking, and payroll for productions.)": "QuickBooks",
    "Do you have training on any of these tools? (Xero: AI-driven accounting platform for tracking production budgets and automating invoicing.)": "Xero",
    "Do you have training on any of these tools? (Vic.ai: Provides AI-powered accounts payable automation, helping with financial data analysis and cost management.)": "Vic.ai",
    "Do you have training on any of these tools? (Expensify: AI automates expense reporting and reimbursement, making it useful for tracking production costs.)": "Expensify",
    "Do you have training on any of these tools? (Runway ML: Allows directors to experiment with real-time visual effects and style transfers, enabling quick visualization of ideas during pre-production or post-production.)": "Runway ML",
    "Do you have training on any of these tools? (ChatGPT (OpenAI): Scriptwriting assistance, brainstorming ideas, and dialogue generation.)": "ChatGPT",
    "Do you have training on any of these tools? (Synthesia: Generate AI-driven video content or virtual actors for pre-visualization and concept testing.)": "Synthesia",
    "Do you have training on any of these tools? (DALL-E 3: Generate detailed concept art and storyboarding from textual descriptions.)": "DALL-E",
    "Do you have training on any of these tools? (Artbreeder: AI-assisted tool for designing character and mood concepts, as well as set backgrounds.)": "Artbreeder",
    "Do you have training on any of these tools? (What3Words + AI Integration: Helps location managers log and communicate precise locations using AI to optimize scouting logistics. )": "What3Words + AI Integration"
}

# Creating df and excel for "Have you heard/used these AI tasks?" question
tasks_heard = df.iloc[:, 19:73]
df_tasks = pd.melt(df, id_vars=id_variables, value_vars=tasks_heard, var_name='AI_Task', value_name='Response').dropna(subset=['Response'])
df_tasks.to_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-AI-Tasks.xlsx')

# Creating df and excel for "Are you concerned about these AI Tasks?" question
concerns = df.iloc[:, 74:129]
df_concerns = pd.melt(df, id_vars=id_variables, value_vars=concerns, var_name='AI_Concerns', value_name='Response').dropna(subset=['Response'])
df_concerns.to_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-AI-Concerns.xlsx')

# Creating df and excel for AI Tools - Have you used them? question
tools_used = df.iloc[:, 136:166]
df_tool_usage = pd.melt(df, id_vars=id_variables, value_vars=tools_used, var_name='Tool', value_name='Response').dropna(subset=['Response'])
df_tool_usage.replace(replacement_dict, inplace=True)
df_tool_usage.to_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-AI-Tools-Used.xlsx')

# Creating df and excel for AI Tools - Have you heard about them? question
tools_heard = df.iloc[:, 168:198]
df_tool_heard = pd.melt(df, id_vars=id_variables, value_vars=tools_heard, var_name='Tool', value_name='Response').dropna(subset=['Response'])
df_tool_heard.replace(others_replacement_dict, inplace=True)
df_tool_heard.to_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-AI-Tools-Heard.xlsx')

# Creating df and excel for AI Tools - Do you want training? question
tools_training = df.iloc[:, 200:230]
df_tool_training = pd.melt(df, id_vars=id_variables, value_vars=tools_training, var_name='Tool', value_name='Response').dropna(subset=['Response'])
df_tool_training.replace(training_replacement_dict, inplace=True)
df_tool_training.to_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-AI-Tools-Training.xlsx')



df1 = pd.read_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-AI-Tasks.xlsx')
df2 = pd.read_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-AI-Concerns.xlsx')
df3 = pd.read_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-AI-Tools-Used.xlsx')
df4 = pd.read_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-AI-Tools-Heard.xlsx')
df5 = pd.read_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-AI-Tools-Training.xlsx')

df1['Type'] = 'Task'
df2['Type'] = 'Concern'
df3['Type'] = 'Tool Usage'
df4['Type'] = 'Tool Colleague Usage'
df5['Type'] = 'Training'


df_concat = pd.concat([df1, df2, df3, df4, df5], ignore_index=True, axis=0)

df_concat.to_excel('/Users/gbeltrami/Desktop/Work/Code/AI-Survey-Results-tr-Tools-Tasks-Complete.xlsx')