import { Client } from "@gradio/client";
import readline from "readline";

const HF_TOKEN = "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"; // required if the space is private

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter an image URL: ", async (imageUrl) => {
  try {
    console.log(`📸 Processing image: ${imageUrl}`);

    // Download the Firebase image as Blob
    const res = await fetch(imageUrl);
    if (!res.ok) throw new Error(`Failed to fetch image: ${res.statusText}`);
    const exampleImage = await res.blob();

    // Connect to HF client
    const client = await Client.connect("fancyfeast/joy-caption-alpha-two", {
      hf_token: HF_TOKEN // add this if needed
    });

    const result = await client.predict("/stream_chat", { 
      input_image: exampleImage,
      caption_type: "Descriptive",
      caption_length: "any",
      extra_options: ["If there is a person/character in the image you must refer to them as {name}."],
      name_input: "User",
      custom_prompt: "Generate a useful caption for this report image"
    });

    console.log("✅ Caption:", result.data[1]);
  } catch (err) {
    console.error("❌ Error:", err);
  } finally {
    rl.close();
  }
});
