function generateSequence(start, end) {
    const startStr = start.toUpperCase();
    const endStr = end.toUpperCase();

    if (startStr.length !== endStr.length || startStr.length < 2) return [startStr, endStr];

    const prefix = startStr.substring(0, startStr.length - 2);
    const prefixEnd = endStr.substring(0, endStr.length - 2);

    if (prefix !== prefixEnd) return [startStr, endStr];

    let s1 = startStr.charAt(startStr.length - 2), s2 = startStr.charAt(startStr.length - 1);
    let e1 = endStr.charAt(endStr.length - 2), e2 = endStr.charAt(endStr.length - 1);

    let all = [];
    // JNTU Sequence: 00 to 99
    for (let i = 0; i <= 9; i++) {
        for (let j = 0; j <= 9; j++) {
            all.push(i.toString() + j.toString());
        }
    }
    // A0 to Z9
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for (let c of letters) {
        for (let j = 0; j <= 9; j++) {
            all.push(c + j.toString());
        }
    }

    const startIndex = all.indexOf(s1 + s2);
    const endIndex = all.indexOf(e1 + e2);

    let result = [];
    if (startIndex !== -1 && endIndex !== -1 && startIndex <= endIndex) {
        for (let i = startIndex; i <= endIndex; i++) {
            result.push(prefix + all[i]);
        }
    } else {
        result = [startStr, endStr];
    }

    return result;
}

try {
    const r1 = generateSequence("246F1A0501", "246F1A05C8");
    const r2 = generateSequence("256F5A0501", "256F5A0512");
    console.log("R1 length:", r1.length);
    console.log("R2 length:", r2.length);
} catch (e) {
    console.error("Error seq:", e);
}
