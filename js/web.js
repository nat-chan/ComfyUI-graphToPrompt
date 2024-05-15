import { app, ComfyApp } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";

app.registerExtension({
    name: "ComfyUI-graphToPrompt",

    async setup() {
        // queuePromptを呼び出すイベントリスナーを追加
        api.addEventListener("run_workflow", async ({ detail }) => {
            await app.loadGraphData(detail);
            let { workflow, workflow_api } = await app.graphToPrompt();
            console.log("workflow", workflow);
            console.log("workflow_api", workflow_api);
            const response = await fetch('http://localhost:8189/graph_to_prompt_from_js', {
                credentials: "same-origin",
                mode: "same-origin",
                method: "post",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(workflow)
            });

            if (!response.ok) {
                console.error('サーバーからの応答がありません。エラー:', response.status);
            } else {
                const responseData = await response.json();
                console.log('サーバーからの応答:', responseData);
            }
        });

    }
})
