import pytest


@pytest.mark.parametrize(
    'text_signature,bytes4_signature',
    (
        ('NewPoll(string,string,uint256,uint256)', '\x00\x10\n\x18'),
        ('computeResponse(uint256,uint16)', '\x00µ²#'),
        ('setLowerFeePercentage(uint8)', '\x00;\x9d\x88'),
        ('setHand(uint256)', '\x00Ç!«'),
        ('comparisonchr(string)', '\x00\x873g'),
        ('getTokenDivisor()', '\x00úôÝ'),
        ('getFrontend()', '\x000tÿ'),
        ('triggerPayment()', '\x00Î W'),
        ('setMinimumPassPercentage(uint8)', '\x00äg\x00'),
    ),
)
def test_00_prefixed_signatures_result_in_correct_4byte_signature(factories,
                                                                  models,
                                                                  text_signature,
                                                                  bytes4_signature):
    signature = factories.SignatureFactory(text_signature=text_signature)

    bytes_signature = models.BytesSignature.objects.get(pk=signature.bytes_signature_id)

    assert len(bytes_signature.bytes4_signature) == 4
    assert bytes_signature.bytes4_signature == bytes4_signature
