// Commands:
//     hubot search <part_of_Log_snippet> - Shows you the  action to do for the alerts

const request = require('request');
 

function testapi(response) {
    // request(apiurl, (err, res, body) => {
    //     if (err) {
    //         res.send("some api error");
    //     }
    //     console.log(body);
    //     response.send(body);
    // });
    let apiurl = 'http://jsonplaceholder.typicode.com/todos/1';
    request({
        url: apiurl,
        method: "GET",
    }, (err, res, body) => {
        if (err) {
            res.send("some api error");
        }
        // console.log(body);
        response.send(body);
    });
}

// function checkelastic(response){
//     es_base_url = 'http://localhost:9200/'
//     index = "runbook_index"
//     doc_type = 'r3d3_type'
//     request(es_base_url, (err, res, body) => {
//         if (err) {
//             response.send(err);
//         }
//         response.send(body);
//     });
// }

function searchelastic(response, term){
    es_base_url = 'http://localhost:9200/'
    index = "runbook_index/"
    doc_type = 'r3d3_type'
    let apiurl = es_base_url + index + doc_type + "/_search";
    j = {
        "query": {
            "match": {
                "Log snippet": term
            }
        }
    }
    request({
        url: apiurl,
        method: "POST",
        json: j
    }, (err, res, body) => {
        if (err) {
            console.log("SOME ERROR: ")
            console.log(err)
            // res.send("some api error");
        }
        data = body["hits"]["hits"]
        result_count = body["hits"]["total"]["value"];
        var result = [];
        for(var i=0; i<data.length; i++) {
            ss = ""
            let source = data[i]["_source"];
            ss += "Cause:\n";
            ss += source["Cause"] + "\n\n";
            ss += "Action To Do:\n";
            ss += source["Action To Do"]
            result.push(ss);
        }
        str_sep = "=".repeat(40);
        result_text = result.join(`\n\n${str_sep}\n\n`)
        output = {
            "text": `Found ${result_count} results` ,
            "attachments": [
                {
                    "text": result_text
                }
            ]
        }
        response.send(output);
    });

    // request(es_base_url, (err, res, body) => {
    //     if (err) {
    //         response.send(err);
    //     }
    //     response.send(body);
    // });
}




module.exports = function(robot) {
    robot.respond(/is this me/i, function(response) {
        testapi(response);
    });

    robot.respond(/search (.+)$/i, function(response) {
        term = response.match[1];
        searchelastic(response, term);

    });

    robot.respond(/who am i/i, function(response) {
        // console.log(response.message.user.name)
        response.send(response.message.user.name)
    });

    robot.respond(/hi (wass|whats) up/i, function(response) {
        // console.log(response.message.user.name)
        response.send("Hey, How may I help you?");
    });

    robot.respond(/who are you?/i, function(response) {
        // console.log(response.message.user.name)
        response.send("I'm your friendly bot");
    });

    robot.respond(/what can you help on ?/i, function(response) {
        // console.log(response.message.user.name)
        response.send("For now, I can only help with r3d3 runbook queries");
    });
}
  
     
  
  