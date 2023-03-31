import cv2
import numpy as np
import argparse
from os.path import basename


def color_transfer(source, target):
    try:
        source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype(np.float32)
        target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype(np.float32)
        srcMean, srcStd = cv2.meanStdDev(source)
        targetMean, targetStd = cv2.meanStdDev(target)
        res = []
        for i, channel in enumerate(cv2.split(target)):
            channel -= targetMean[i]
            channel *= srcStd[i] / targetStd[i]
            channel += srcMean[i]
            res.append(np.clip(channel, 0, 255).astype("uint8"))
        result = cv2.merge(res)
        return cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
    except Exception as e:
        print("Error: " + str(e))
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        "-s",
        required=True,
        help="Path of image from whose color texture is being used",
    )
    parser.add_argument(
        "--target",
        "-t",
        required=True,
        help="Path of image on color texture is being applied",
    )
    parser.add_argument("--result", "-r", help="Path of result image")
    parser.add_argument(
        "--visualize", "-v", help="Visualize the result", action="store_true"
    )
    args = vars(parser.parse_args())

    source = cv2.imread(args["source"])
    target = cv2.imread(args["target"])
    result = color_transfer(source, target)

    if args["result"]:
        cv2.imwrite(args["result"], result)
        print("Result saved at: " + args["result"])
    else:
        cv2.imwrite(
            basename(args["source"]).split(".")[0]
            + "_"
            + basename(args["target"]).split(".")[0]
            + ".jpg",
            result,
        )
        print(
            "Result saved at: "
            + basename(args["source"]).split(".")[0]
            + "_"
            + basename(args["target"]).split(".")[0]
            + ".jpg"
        )

    if args["visualize"]:
        source = cv2.resize(source, (300, 300))
        target = cv2.resize(target, (300, 300))
        result = cv2.resize(result, (300, 300))
        cv2.putText(
            source, "Source", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
        )
        cv2.putText(
            target, "Target", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
        )
        cv2.putText(
            result, "Result", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
        )
        np.hstack([source, target, result])
        cv2.imshow("Press 'q' to exit", np.hstack([source, target, result]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
