# Week 8 Overview Video Script

---

Hello everyone, and welcome to Week 8 of Introduction to Machine Learning with Python.

This week is your Chapter 2 capstone. There is no new reading, no demo, and no quiz. Instead, you have one assignment: a predictive maintenance consultation where you advise a plant manager named Rivera on building a system to predict machine failures. Your deliverable is a video presenting your recommendation.

This is different from Weeks 4 and 6. In those weeks, you were given tables of results and asked to interpret them. This week, there are no pre-built results. You are given a problem, a dataset description, and a stakeholder who needs answers. The assignment walks you through five sections. You start by defining the problem and recommending an algorithm, then move into explaining how the model communicates confidence in its predictions, including two different methods for doing that. The final section brings it together with interpretability and a practical recommendation for a case where the model is uncertain. Each section builds on the one before it, and the reasoning throughout is yours.

Before you start, I want to flag something important. The assignment introduces a cost structure where missing a real machine failure costs roughly eight times more than pulling a machine unnecessarily. This concept, cost asymmetry, is new. You have not seen it before in this course. The assignment includes a primer that explains it, so read that section carefully. Do not skim it. The cost structure is not just one question. It threads through your entire video. How you talk about prediction confidence, how you handle uncertain predictions, what you recommend for a machine the model is unsure about, all of that connects back to the cost structure. If you skip over it, the rest of your reasoning will not hold together.

The other thing to keep in mind is scope. Weeks 4 and 6 tested the concepts from the immediately prior week. This assignment draws on all of Chapter 2. The algorithm recommendation section requires you to understand the strengths and limitations of different algorithms well enough to justify a choice for Rivera's specific data. The confidence sections require you to know how scikit-learn provides uncertainty information beyond a basic prediction label, which was the focus of Week 7. The interpretability section requires you to explain what tools your algorithm provides for understanding which features drive predictions and what those tools can and cannot show, which connects back to Weeks 3 and 5. If you only review Week 7 materials, you will be underprepared. Go back to your prior demo notebooks and overview pages as needed.

One more thing. You are presenting to Rivera, not to me. Rivera is a plant manager, not a data scientist. When you explain how the model communicates confidence, think about what Rivera needs to hear to make decisions, not what would earn points on a quiz. There is a difference between saying "this method returns class probabilities bounded between zero and one" and saying "instead of just telling you a machine will fail, the model tells you there is a 91% chance it will fail, and you can use that number to decide how urgently to act." The first is a definition. The second is something Rivera can use. If you find yourself reciting definitions, step back and ask whether Rivera would understand what you just said and whether he could act on it.

So for this week: review your prior materials as needed, read through the full assignment carefully including the cost structure primer and the sample data, and then record your video addressing all five sections.

Alright, that's it for the Week 8 overview. Good luck with the capstone.
